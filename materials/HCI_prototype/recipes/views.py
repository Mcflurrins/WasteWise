from django.shortcuts import render, get_object_or_404
from expiry_tracker.models import FoodItem
from .models import Recipe, Ingredient

def recommend_recipes(request):
    # Get the user's owned ingredients
    # (if you have per-user data, add .filter(user=request.user))
    user_items = FoodItem.objects.all()

    # Collect ingredient objects linked to user's food items
    user_ingredients = Ingredient.objects.filter(food_items__in=user_items).distinct()

    # Get all recipes
    recipes = Recipe.objects.prefetch_related("ingredients").all()

    recommended = []

    for recipe in recipes:
        recipe_ingredients = recipe.ingredients.all()
        matching = [ing for ing in recipe_ingredients if ing in user_ingredients]
        if matching:
            recommended.append({
                "recipe": recipe,
                "matches": matching,
                "match_count": len(matching),
            })

    # Sort by most matched ingredients
    recommended.sort(key=lambda r: r["match_count"], reverse=True)

    return render(request, "recommended_recipes.html", {"recommended": recommended})


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, "recipe_detail.html", {"recipe": recipe})
