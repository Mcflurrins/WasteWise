from django.urls import path
from . import views

app_name = "recipes"

urlpatterns = [
    path("recommend/", views.recommend_recipes, name="recommend"),
    path("<int:pk>/", views.recipe_detail, name="detail"),
]
