from rest_framework import viewsets
from .models import Recipe
from .serializer import RecipeSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Recipe operations.
    
    Provides CRUD (Create, Read, Update, Delete) operations for Recipe objects
    through RESTful API endpoints. Automatically generates the following endpoints:
    - GET /recipes/ - List all recipes
    - POST /recipes/ - Create a new recipe
    - GET /recipes/{id}/ - Retrieve a specific recipe
    - PUT /recipes/{id}/ - Update a specific recipe
    - DELETE /recipes/{id}/ - Delete a specific recipe
    
    Attributes:
        queryset: QuerySet containing all Recipe objects
        serializer_class: Serializer used for data validation and conversion
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer