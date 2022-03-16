from django.shortcuts import get_object_or_404, render

from .models import Recipe

def index(request):
    recipe = Recipe.objects.order_by('-list_date').filter(is_published=True)

    context = {
        'recipes': recipe
    }
    return render(request, 'recipes/recipes.html', context)

def recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    context = {
        'recipe': recipe
    }

    return render(request, 'recipes/recipe.html', context)

def search(request):
    return render(request, 'recipes/search.html')
