from rest_framework import serializers
from recipe.models import *
from ingredients.models import *
from ingredients.serializers import IngredientSerializer


class RecipeSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=150, allow_null=False, allow_blank=False)
    description = serializers.CharField()
    preparation_process = serializers.CharField(max_length=255)
    serving_idea = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    ingredient = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ["id", "title", "description", "preparation_process", "serving_idea",  "created_at", "updated_at",
                   "ingredient"]

    def update(self, instance, validated_data):
        print(validated_data)
        print(validated_data["ingredient"])
        for i in validated_data["ingredient"]:
            Ingredient.objects.get(id=i["id"])
            instance.ingredient.add(Ingredient.objects.get(id=i["id"]))
        return instance
