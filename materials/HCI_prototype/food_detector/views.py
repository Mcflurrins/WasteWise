from django.shortcuts import render

# Create your views here.
def show_food_detector(request):
    return render(request, 'food_detector.html')

# myapp/views.py
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from PIL import Image
import io, base64
import numpy as np
from ultralytics import YOLO
from django.utils import timezone
from datetime import timedelta
from expiry_tracker.models import FoodItem

model = YOLO('yolov8n.pt')  # replace with your custom trained model if needed

@csrf_exempt
def detect(request):
    if request.method == 'POST':
        image_file = request.FILES.get('image')
        if not image_file:
            return JsonResponse({"error": "No image uploaded"}, status=400)
        
        image = Image.open(image_file).convert('RGB')
        results = model(np.array(image))  # YOLO inference
        detections = []

        # Loop through results
        for box in results[0].boxes.data.tolist():  # [x1,y1,x2,y2,score,class_id]
            detections.append({
                "bbox": box[:4],
                "confidence": box[4],
                "class_id": int(box[5]),
                "label": results[0].names[int(box[5])]
            })

        return JsonResponse({"detections": detections})
    
    return JsonResponse({"error": "Invalid method"}, status=405)

@csrf_exempt
def save_snapshot(request):
    if request.method == 'POST':
        image_file = request.FILES.get('image')
        if not image_file:
            return JsonResponse({"error": "No image uploaded"}, status=400)
        
        image = Image.open(image_file).convert('RGB')
        results = model(np.array(image))

        # detected labels (strings)
        detections = [results[0].names[int(box[5])] for box in results[0].boxes.data.tolist()]

        pantry_updates = []
        today = timezone.localdate()
        default_expiry = today + timedelta(days=7)  # adjust policy as needed

        for label in detections:
            name = label.strip()
            if not name:
                continue
            # Normalize: store title-cased name
            canonical = name.title()

            # Try to find existing pantry item (case-insensitive)
            existing = FoodItem.objects.filter(name__iexact=canonical).first()
            if existing:
                # simple policy: increment quantity by 1 and touch created_at/last seen via save()
                existing.quantity = existing.quantity + 1
                existing.save()
                pantry_updates.append({
                    "id": existing.id,
                    "name": existing.name,
                    "action": "updated",
                    "quantity": existing.quantity,
                    "expiry_date": existing.expiry_date.isoformat() if existing.expiry_date else None
                })
            else:
                # create new item with a default expiry (required by model)
                created = FoodItem.objects.create(
                    name=canonical,
                    quantity=1,
                    unit="",
                    storage="",
                    expiry_date=default_expiry,
                    dietary=[],
                    notes="Auto-added from snapshot"
                )
                pantry_updates.append({
                    "id": created.id,
                    "name": created.name,
                    "action": "created",
                    "quantity": created.quantity,
                    "expiry_date": created.expiry_date.isoformat()
                })

        return JsonResponse({"detections": detections, "pantry_updates": pantry_updates})
    return JsonResponse({"error": "Invalid method"}, status=405)

def snapshot_result(request):
    objects_json = request.GET.get('objects', '[]')
    import json
    try:
        objects = json.loads(objects_json)
    except Exception:
        objects = []

    # Normalize objects into the form the template expects: list of {'label': ...}
    detections = []
    for o in objects:
        if isinstance(o, dict):
            if 'label' in o:
                detections.append({'label': o['label']})
            elif 'name' in o:
                detections.append({'label': o['name']})
            else:
                detections.append({'label': str(o)})
        else:
            detections.append({'label': str(o)})

    return render(request, 'snapshot_result.html', {"detections": detections})

import json
from django.http import JsonResponse
from django.test import RequestFactory
from django.views.decorators.csrf import csrf_exempt
from expiry_tracker.views import add_food as expiry_add_food
from django.http import QueryDict


@csrf_exempt
def import_to_expiry(request):
    """
    Accept JSON { items: [ {name, quantity, unit, storage, expiry_date, dietary, notes}, ... ] }
    For each item, create a POST request and call expiry_tracker.views.add_food(request).
    Returns JSON success/failure.
    """
    if request.method != "POST":
        return JsonResponse({"success": False, "error": "POST required"}, status=405)

    try:
        payload = json.loads(request.body.decode("utf-8") or "{}")
    except Exception:
        return JsonResponse({"success": False, "error": "invalid json"}, status=400)

    items = payload.get("items", [])
    rf = RequestFactory()
    success_count = 0
    errors = []

    for idx, item in enumerate(items):
        # Normalize and build POST data
        post_data = QueryDict(mutable=True)
        post_data.update({
            "name": item.get("name", ""),
            "quantity": str(item.get("quantity", "1")),
            "unit": item.get("unit", ""),
            "storage": item.get("storage", ""),
            "expiry_date": item.get("expiry_date", ""),
            "notes": item.get("notes", ""),
        })

        # Handle dietary list properly
        dietary_value = item.get("dietary", [])
        if isinstance(dietary_value, str):
            dietary_list = [d.strip() for d in dietary_value.split(",") if d.strip()]
        elif isinstance(dietary_value, (list, tuple)):
            dietary_list = [str(d).strip() for d in dietary_value if str(d).strip()]
        else:
            dietary_list = []
        for tag in dietary_list:
            post_data.update({"dietary": tag})

        # Create fake POST request
        new_req = rf.post("/expiry_tracker/add/", data=post_data)
        new_req.user = getattr(request, "user", None)

        # Directly call the add_food view
        resp = expiry_add_food(new_req)
        if resp.status_code in (301, 302):  # redirect = success
            success_count += 1
        else:
            errors.append({"index": idx, "data": item})

    return JsonResponse({
        "success": True,
        "inserted": success_count,
        "failed": len(errors),
        "errors": errors,
    })
