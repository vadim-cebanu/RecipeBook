from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User


class RecipeAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("recipes-list")
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        
    def test_get_recipes_list_returns_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_create_recipe_returns_201(self):
        
        data ={
                'title' : 'test title',
                'description' : 'test description',
                'created_at' : 'created test',
                'author' : self.user.id
        }
                
           
        response = self.client.post(self.url, data, format='json')
            
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
