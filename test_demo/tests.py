from django.test import TestCase
from app.demo import add

class DemoTests(TestCase):
    def test_add(self):
        self.assertEqual(add(2,2),4)