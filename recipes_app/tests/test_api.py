from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from recipes_app.models import Recipe
from rest_framework.authtoken.models import Token


class RecipeAPITestCaseUnhappy(TestCase):
    """
    Test case for unhappy path scenarios in the Recipe API.
    
    Tests various error conditions and unauthorized access attempts
    to ensure proper security and error handling.
    """
    
    def setUp(self):
        """
        Set up test fixtures before each test method.
        
        Creates an unauthenticated API client and stores the list URL.
        """
        self.client = APIClient()
        self.list_url = reverse("recipes-list")

    def test_get_recipes_list_without_auth_returns_401(self):
        """
        Test that accessing recipe list without authentication returns 401.
        
        Verifies that the API properly protects recipe data and requires
        authentication before allowing access to the recipe list.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_without_auth_returns_401(self):
        """
        Test that creating a recipe without authentication returns 401.
        
        Ensures that unauthenticated users cannot create new recipes,
        even with valid recipe data.
        """
        user = User.objects.create_user(username="testuser", password="testpassword123")
        data = {
            "title": "Test Recipe",
            "description": "A delicious recipe",
            "author": user.id,
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class RecipeAPITestCaseHappy(TestCase):
    """
    Test case for happy path scenarios in the Recipe API.
    
    Tests successful operations with proper authentication to ensure
    the API functions correctly for authorized users.
    """
    
    def setUp(self):
        """
        Set up test fixtures before each test method.
        
        Creates an authenticated API client with a test user and token.
        This setup is used for all happy path test scenarios.
        """
        self.client = APIClient()
        self.list_url = reverse("recipes-list")
        self.user = User.objects.create_user(
            username="testuser", password="testpassword123"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def test_get_recipes_list_with_auth_returns_200(self):
        """
        Test that authenticated users can successfully retrieve recipe list.
        
        Verifies that the API returns HTTP 200 OK status when an authenticated
        user requests the list of recipes.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_as_logged_in_user_returns_201(self):
        """
        Test that authenticated users can successfully create a new recipe.
        
        Verifies that:
        - The API returns HTTP 201 CREATED status
        - The recipe is actually saved to the database
        """
        data = {
            "title": "Happy Path Recipe",
            "description": "Created by logged-in user",
            "author": self.user.id,
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Recipe.objects.count(), 1)

    def test_get_recipe_detail_as_logged_in_user_returns_200(self):
        """
        Test that authenticated users can retrieve a specific recipe's details.
        
        Creates a test recipe and verifies that an authenticated user can
        successfully fetch its details via the detail endpoint.
        """
        recipe = Recipe.objects.create(
            title="Detail Test Recipe",
            description="Description",
            author=self.user,
        )
        detail_url = reverse("recipes-detail", kwargs={"pk": recipe.id})
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)