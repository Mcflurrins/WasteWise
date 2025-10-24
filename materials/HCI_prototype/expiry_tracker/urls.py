from django.urls import path
from . import views

app_name = "expiry_tracker"

urlpatterns = [
    path("", views.add_food, name="add"),
    path("list/", views.list_items, name="list"),
    path("delete/<int:pk>/", views.delete_item, name="delete"),
]