from django.db import models
from datetime import datetime

class Employer(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
