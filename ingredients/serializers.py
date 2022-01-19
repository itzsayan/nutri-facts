from rest_framework import serializers
from ingredients.models import *


class IngredientSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=150, allow_blank=False, allow_null=False)
    description = serializers.CharField()
    side_effects = serializers.CharField()
    benefit = serializers.CharField()
    calorie = serializers.IntegerField()
    price = serializers.CharField(max_length=150, allow_blank=False, allow_null=False)
    category_name = serializers.CharField(max_length=50, allow_blank=False, allow_null=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Ingredient
        fields = ["id", "name", "description", "side_effects", "benefit", "calorie", "price", "category_name",
                  "created_at", "updated_at"]

    def update(self, instance, validated_data):
        print(validated_data)
