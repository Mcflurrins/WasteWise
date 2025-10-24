from django.db import models
from recipes.models import Ingredient  # import this at the top
class FoodItem(models.Model):
    name = models.CharField(max_length=200)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.SET_NULL, null=True, blank=True, related_name="food_items")
    quantity = models.PositiveIntegerField(default=1)
    unit = models.CharField(max_length=32, blank=True)
    storage = models.CharField(max_length=64, blank=True)
    expiry_date = models.DateField()
    dietary = models.JSONField(default=list, blank=True)  # stores list of dietary tags
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.quantity}{self.unit or ''})"
# in recipes/models.py

