from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    """
    Recipe model representing a cooking recipe in the application.
    
    Attributes:
        title (CharField): The title of the recipe (max 100 characters)
        description (TextField): Detailed description of the recipe
        created_at (DateTimeField): Timestamp when the recipe was created
        author (ForeignKey): Reference to the User who created the recipe
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        String representation of the Recipe object.
        
        Returns:
            str: The title of the recipe
        """
        return self.title