from django.contrib import admin

# Register your models hfrom django.contrib import admin
from .models import Recipe, Ingredient

admin.site.register(Recipe)
admin.site.register(Ingredient)

