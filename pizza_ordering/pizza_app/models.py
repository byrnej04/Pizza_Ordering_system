from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from decimal import Decimal
from datetime import timedelta

class PizzaSize(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('0.00'))
    def __str__(self):
        return self.name

class Cheese(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('0.00'))
    def __str__(self):
        return self.name

class Sauce(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('0.00'))
    def __str__(self):
        return self.name

class Crust(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('0.00'))
    def __str__(self):
        return self.name

class Topping(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal('0.00'))
    def __str__(self):
        return self.name

class Pizza(models.Model):
    size = models.ForeignKey(PizzaSize, on_delete=models.SET_NULL, null=True)
    crust = models.ForeignKey(Crust, on_delete=models.SET_NULL, null=True)
    sauce = models.ForeignKey(Sauce, on_delete=models.SET_NULL, null=True)
    cheese = models.ForeignKey(Cheese, on_delete=models.SET_NULL, null=True)
    toppings = models.ManyToManyField(Topping, blank=True)
    def __str__(self):
        return f"{self.size} pizza"
    @property
    def total_price(self):
        total = Decimal('0.00')
        if self.size: total += self.size.price
        if self.crust: total += self.crust.price
        if self.sauce: total += self.sauce.price
        if self.cheese: total += self.cheese.price
        for t in self.toppings.all():
            total += t.price
        return total

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pizzas = models.ManyToManyField(Pizza)
    customer_name = models.CharField(max_length=100)
    address = models.TextField()
    card_number = models.CharField(max_length=16)
    card_expiry_month = models.CharField(max_length=2)
    card_expiry_year = models.CharField(max_length=4)
    card_cvv = models.CharField(max_length=3)
    order_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"
    @property
    def total_order_price(self):
        return sum(p.total_price for p in self.pizzas.all())
    @property
    def expected_delivery_time(self):
        return self.order_date + timedelta(minutes=30)
