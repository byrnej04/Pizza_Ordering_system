from django.contrib import admin
from .models import PizzaSize, Cheese, Sauce, Crust, Topping, Pizza, Order

admin.site.register(PizzaSize)
admin.site.register(Cheese)
admin.site.register(Sauce)
admin.site.register(Crust)
admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(Order)
