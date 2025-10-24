from django import forms
from .models import FoodItem

DIETARY_CHOICES = [
    ("vegetarian", "Vegetarian"),
    ("vegan", "Vegan"),
    ("gluten_free", "Gluten-free"),
    ("dairy_free", "Dairy-free"),
    ("nut_free", "Nut-free"),
]

class FoodItemForm(forms.ModelForm):
    dietary = forms.MultipleChoiceField(
        choices=DIETARY_CHOICES,
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
    expiry_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))

    class Meta:
        model = FoodItem
        fields = ["name", "quantity", "unit", "storage", "expiry_date", "dietary", "notes"]