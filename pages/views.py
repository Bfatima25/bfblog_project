from django.shortcuts import render
from django.http import HttpResponse
from recipes.models import Recipe
from employers.models import Employer

def index(request):
    recipes = Recipe.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'recipes': recipes
    }

    return render(request, 'pages/index.html', context)

def about(request):
    #Get all employers
    employers = Employer.objects.order_by('-hire_date')

    context = {
        'employers': employers,
    }
    return render(request, 'pages/about.html', context)
