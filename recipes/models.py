from django.db import models
from datetime import datetime
from employers.models import Employer

class Recipe(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.DO_NOTHING, default=None)
    title = models.CharField(max_length=200)
    Specialdiet = models.CharField(max_length=50, null=True)
    Mealtype = models.CharField(max_length=50, null=True)
    preptime = models.CharField(max_length=50)
    totaltime = models.CharField(max_length=50)
    Ingredients = models.TextField(max_length=1000)
    Directions = models.TextField(max_length=1000)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
