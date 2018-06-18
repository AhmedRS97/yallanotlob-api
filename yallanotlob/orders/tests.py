from django.test import TestCase
from .models import Meal, Order

# Create your tests here.
class MealModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Meal.objects.create(name='First Meal')
        Meal.objects.create(description='Description for Meal')

    def test_title_content(self):
        meal = Meal.objects.get(id=1)
        expected_object_name = f'{meal.name}'
        self.assertEquals(expected_object_name, 'First Meal')

    def test_description_content(self):
        meal = Meal.objects.get(id=2)
        expected_object_name = f'{meal.description}'
        self.assertEquals(expected_object_name, 'Description for Meal')
