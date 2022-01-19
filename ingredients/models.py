from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField()
    side_effects = models.TextField()
    benefit = models.TextField()
    calorie = models.IntegerField(blank=False)
    price = models.CharField(max_length=50, blank=False, null=False)
    category_name = models.CharField(max_length=50, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, default=None)
