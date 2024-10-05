from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework import test, status
from rest_framework.test import APIClient
from django.urls import reverse
from core.models import Ingredient, Recipe, Tag
from recipe.serializers import RecipeDetailSerializer, RecipeSerializer

RECIPES_URL = reverse('recipe:recipe-list')

# recipe/recipes/<id>


def get_detail_url(recipe_id):
    print(recipe_id)
    return reverse('recipe:recipe-detail', args=[recipe_id])


def generate_sample_tag(user, name='Main tag'):
    return Tag.objects.create(user=user, name=name)


def generate_sample_ingredient(user, name='Main tag', amount=10):
    return Ingredient.objects.create(user=user, name=name, amount=amount)


def generate_sample_recipe(user, **params):
    defaults = {
        'title': 'Sample Recipe',
        'time_minutes': 999,
        'cost': 5.00
    }
    defaults.update(params)
    return Recipe.objects.create(user=user, **defaults)


class PublicRecipeApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(RECIPES_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateRecipeApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test@sample.com',
            'testpass'
        )
        self.client.force_authenticate(self.user)

    def test_get_recipes(self):
        generate_sample_recipe(user=self.user)
        generate_sample_recipe(user=self.user)
        generate_sample_recipe(user=self.user)

        res = self.client.get(RECIPES_URL)
        recipes = Recipe.objects.all().order_by('-title')
        serializer = RecipeSerializer(recipes, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_view_recipe_detail(self):
        recipe = generate_sample_recipe(user=self.user)
        recipe.tags.add(generate_sample_tag(user=self.user))
        recipe.ingredients.add(generate_sample_ingredient(user=self.user))
        
        res = self.client(get_detail_url(recipe_id=recipe.id))
        serializer = RecipeDetailSerializer(recipe, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)