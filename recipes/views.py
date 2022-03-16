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
    queryset_list = Recipe.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(Directions__icontains=keywords)
        
    # Meal Type
    if 'meal' in request.GET:
        meal = request.GET['meal']
        if meal:
            queryset_list = queryset_list.filter(Mealtype__iexact=meal)
    
    # Special Diet
    if 'diet' in request.GET:
        diet = request.GET['diet']
        if diet:
            queryset_list = queryset_list.filter(Specialdiet__iexact=diet)

    context = {
        'search': recipe,
        'recipes': queryset_list
    }
    

    return render(request, 'recipes/search.html', context)