from rest_framework import serializers
from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Recipe model.
    
    Converts Recipe model instances to JSON format and validates incoming data.
    Handles serialization of all recipe fields including id, title, description,
    creation timestamp, and author information.
    """
    class Meta:
        model = Recipe
        fields = ["id", "title", "description", "created_at", "author"]