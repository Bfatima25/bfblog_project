from django.shortcuts import render

def index(request):
    return render(request, 'recipes/recipes.html')

def recipe(request):
    return render(request, 'recipes/recipe.html')

def search(request):
    return render(request, 'recipes/search.html')
