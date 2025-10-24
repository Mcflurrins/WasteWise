import csv
import json
from django.core.management.base import BaseCommand
from recipes.models import Recipe, Ingredient

class Command(BaseCommand):
    help = "Import recipes and ingredients from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument("csv_path", type=str, help="Path to the CSV file")

    def handle(self, *args, **options):
        csv_path = options["csv_path"]

        with open(csv_path, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                title = row.get("title", "").strip()
                if not title:
                    self.stdout.write(self.style.WARNING("Skipping row with no title"))
                    continue

                description = row.get("description", "").strip()
                steps = row.get("steps", "").strip()
                image_url = row.get("image_url", "").strip()

                # Parse dietary tags — handle JSON or comma-separated
                raw_tags = row.get("dietary_tags", "").strip()
                try:
                    dietary_tags = json.loads(raw_tags) if raw_tags.startswith("[") else [t.strip() for t in raw_tags.split(",") if t.strip()]
                except Exception:
                    dietary_tags = []

                # Create or update recipe
                recipe, created = Recipe.objects.get_or_create(title=title, defaults={
                    "description": description,
                    "steps": steps,
                    "dietary_tags": dietary_tags,
                    "image_url": image_url,
                })

                if not created:
                    recipe.description = description
                    recipe.steps = steps
                    recipe.dietary_tags = dietary_tags
                    recipe.image_url = image_url
                    recipe.save()

                # Handle ingredients
                ingredients_raw = row.get("ingredients", "")
                if ingredients_raw:
                    ingredients = [i.strip().lower() for i in ingredients_raw.split(",") if i.strip()]
                    for ing_name in ingredients:
                        ingredient, _ = Ingredient.objects.get_or_create(name=ing_name)
                        recipe.ingredients.add(ingredient)

                recipe.save()
                self.stdout.write(self.style.SUCCESS(f"Imported: {title}"))
