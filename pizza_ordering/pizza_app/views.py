from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import PizzaForm, OrderForm
from .models import Order, Pizza

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('order_overview')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})

def custom_logout(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('login')

@login_required
def order_overview(request):
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    return render(request, 'order_overview.html', {'orders': orders})

@login_required
def create_pizza(request):
    if request.method == 'POST':
        form = PizzaForm(request.POST)
        if form.is_valid():
            pizza = form.save()
            cart = request.session.get('cart', [])
            cart.append(pizza.id)
            request.session['cart'] = cart
            return redirect('cart')
    else:
        form = PizzaForm()
    return render(request, 'create_pizza.html', {'form': form})


@login_required
def cart(request):
    cart_ids = request.session.get('cart', [])
    pizzas = Pizza.objects.filter(id__in=cart_ids)
    total_cart_price = sum(p.total_price for p in pizzas)
    return render(request, 'cart.html', {'pizzas': pizzas, 'total_cart_price': total_cart_price})

@login_required
def order_details(request):
    cart_ids = request.session.get('cart', [])
    pizzas = Pizza.objects.filter(id__in=cart_ids)
    total_order_price = sum(p.total_price for p in pizzas)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            order.pizzas.set(pizzas)
            del request.session['cart']
            return redirect('order_confirmation', order_id=order.id)
    else:
        form = OrderForm()
    return render(request, 'order_details.html', {'form': form, 'pizzas': pizzas, 'total_order_price': total_order_price})

@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'order_confirmation.html', {'order': order})
