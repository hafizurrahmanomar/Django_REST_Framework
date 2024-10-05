from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@example.com', password='testpass'):
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    def test_ingredient_model(self):
        ingredient = models.Ingredient.objects.create(
            name='Salt',
            amount=1,
            user=sample_user()
        )

        self.assertEqual(str(ingredient), f"{ingredient.name} {ingredient.amount}")

    def test_recipe_model(self):
        recipe = models.Recipe.objects.create(
            title='Chicken Khichuri',
            time_minutes=20,
            cost=150.50,
            user=sample_user()
        )
        
        self.assertEqual(str(recipe), recipe.title)