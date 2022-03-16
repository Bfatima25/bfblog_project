from django.shortcuts import render

from .models import Recipe

def index(request):
    recipe = Recipe.objects.order_by('-list_date').filter(is_published=True)

    context = {
        'recipes': recipe
    }
    return render(request, 'recipes/recipes.html', context)

def recipe(request, recipe_id):
    return render(request, 'recipes/recipe.html')

def search(request):
    return render(request, 'recipes/search.html')
