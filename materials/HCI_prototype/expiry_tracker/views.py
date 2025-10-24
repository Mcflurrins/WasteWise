from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .forms import FoodItemForm
from .models import FoodItem
from recipes.models import Ingredient

def add_food(request):
    if request.method == "POST":
        form = FoodItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.dietary = form.cleaned_data.get("dietary", [])
            ing, _ = Ingredient.objects.get_or_create(name=item.name.lower())
            item.ingredient = ing
            item.save()
            return redirect("expiry_tracker:list")
    else:
        form = FoodItemForm()
    return render(request, "expiry_tracker.html", {"form": form})

def list_items(request):
    items = FoodItem.objects.order_by("-created_at")
    return render(request, "list.html", {"items": items})

@require_POST
def delete_item(request, pk):
    item = get_object_or_404(FoodItem, pk=pk)
    item.delete()
    return redirect("expiry_tracker:list")
