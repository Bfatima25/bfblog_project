from django.shortcuts import render

from .models import Recipe

def index(request):
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes
    }
    return render(request, 'recipes/recipes.html', context)

def recipe(request):
    return render(request, 'recipes/recipe.html')

def search(request):
    return render(request, 'recipes/search.html')
