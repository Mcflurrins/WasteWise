from django.urls import path
from food_detector.views import show_food_detector, detect, save_snapshot, snapshot_result, import_to_expiry

app_name = 'food_detector'

urlpatterns = [
    path('', show_food_detector, name='show_food_detector'),
    path('detect/', detect, name='detect'),
    path('save_snapshot/', save_snapshot, name='save_snapshot'),
    path('snapshot_result/', snapshot_result, name='snapshot_result'),
    path('import_to_expiry/', import_to_expiry, name='import_to_expiry'),

]