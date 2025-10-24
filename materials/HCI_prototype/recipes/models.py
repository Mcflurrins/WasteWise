from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    ingredients = models.ManyToManyField(Ingredient, related_name="recipes", blank=True)
    steps = models.TextField()
    dietary_tags = models.JSONField(default=list, blank=True)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.title