from django.contrib import admin
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'list_date', 'employer')
    list_display_links = ('id', 'title')
    list_filter = ('employer',)
    search_fields = ('title', 'Ingredients', 'Directions', 'Specialdiet', 'Mealtype', 'preptime', 'totaltime')
    list_per_page = 20
admin.site.register(Recipe, RecipeAdmin)
