from django.test import TestCase
from django.contrib.auth.models import User
from .models import PizzaSize, Pizza

class PizzaTest(TestCase):
    def test_total_price(self):
        size = PizzaSize.objects.create(name="Medium", price="10.00")
        pizza = Pizza.objects.create(size=size)
        self.assertEqual(pizza.total_price, 10.00)
