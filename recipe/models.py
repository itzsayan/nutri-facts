from django.db import models
from ingredients.models import *


class Recipe(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField()
    preparation_process = models.TextField()
    serving_idea = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, default=None)
    ingredient = models.ManyToManyField(to=Ingredient, related_name='recipe')
