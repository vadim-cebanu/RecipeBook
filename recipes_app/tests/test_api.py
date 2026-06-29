from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from recipes_app.models import Recipe
from rest_framework.authtoken.models import Token


class RecipeAPITestCaseUnhappy(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.list_url = reverse("recipes-list")

    def test_get_recipes_list_without_auth_returns_401(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_without_auth_returns_401(self):
        data = {
            "title": "Test Recipe",
            "description": "A delicious recipe",
            "author": 1,
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class RecipeAPITestCaseHappy(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.list_url = reverse("recipes-list")
        self.user = User.objects.create_user(
            username="happyuser", password="testpassword123"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def test_get_recipes_list_with_auth_returns_200(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_as_logged_in_user_returns_201(self):
        data = {
            "title": "Happy Path Recipe",
            "description": "Created by logged-in user",
            "author": self.user.id,
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Recipe.objects.count(), 1)

    def test_get_recipe_detail_as_logged_in_user_returns_200(self):
        recipe = Recipe.objects.create(
            title="Detail Test Recipe",
            description="Description",
            author=self.user,
        )
        detail_url = reverse("recipes-detail", kwargs={"pk": recipe.id})
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)