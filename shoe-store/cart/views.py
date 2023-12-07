from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from products.models import ProductModel  
from .models import Cart, CartItem, Checkout, OrderItem
from .forms import CustomPaymentForm 
from functools import wraps





def add_to_cart(request, product_id):
    product = get_object_or_404(ProductModel, id=product_id)

    # Check if user is authenticated
    if request.user.is_authenticated:
        # For authenticated users, use their user instance
        cart, _ = Cart.objects.get_or_create(user=request.user)
    else:
        # For anonymous users, use their session key
        session_key = request.session.session_key or request.session.create()
        cart, _ = Cart.objects.get_or_create(session_key=session_key)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
    else:
        cart_item.quantity = 1

    cart_item.save()
    messages.success(request, "Product added to cart successfully.")
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = None

    if request.user.is_authenticated:
        # For authenticated users, find the cart by user
        cart = Cart.objects.filter(user=request.user).first()
    else:
        # For anonymous users, find the cart by session key
        session_key = request.session.session_key
        if session_key:
            cart = Cart.objects.filter(session_key=session_key).first()

    cart_items = CartItem.objects.filter(cart=cart) if cart else []
    total_cost = sum(item.sub_total() for item in cart_items) if cart else 0

    context = {
        'cart': cart,
        'cart_items': cart_items,
        'total_cost': total_cost,
    }
    return render(request, 'cart_detail.html', context)




def remove_from_cart(request, product_id):
    cart = None

    if request.user.is_authenticated:
        # For authenticated users, find the cart by user
        cart = Cart.objects.filter(user=request.user).first()
    else:
        # For anonymous users, find the cart by session key
        session_key = request.session.session_key
        if session_key:
            cart = Cart.objects.filter(session_key=session_key).first()

    if not cart:
        return redirect('cart:cart_detail')

    product = get_object_or_404(ProductModel, id=product_id)
    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except CartItem.DoesNotExist:
        pass

    return redirect('cart:cart_detail')

@login_required
def checkout(request):
    user = request.user
    cart = Cart.objects.filter(user=user).first()
    
    if not cart:
        messages.info(request, "Your cart is empty.")
        return redirect('cart:cart_detail')

    cart_items = CartItem.objects.filter(cart=cart)
    
    if not cart_items.exists():
        messages.info(request, "Your cart is empty.")
        return redirect('cart:cart_detail')

    cart_total = sum(item.sub_total() for item in cart_items)
    
    if request.method == "POST":
        payment_form = CustomPaymentForm(request.POST)
        
        if payment_form.is_valid():
            # Create a new Checkout instance
            checkout_instance = Checkout(
                user=user,
                order_total=cart_total,
                payment_option=payment_form.cleaned_data['payment_option'],
                delivery_address=payment_form.cleaned_data['delivery_address'],
            )
            checkout_instance.save()

            # Create OrderItem instances for each CartItem
            for cart_item in cart_items:
                OrderItem.objects.create(
                    order=checkout_instance,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    price=cart_item.product.price
                )

            # Clear the cart
            cart_items.delete()
            cart.delete()

            return redirect('cart:order_confirmation') 
    else:
        payment_form = CustomPaymentForm()

    context = {
        'payment_form': payment_form,
        'cart_total': cart_total,
        'cart_items': cart_items
    }
    return render(request, 'checkout.html', context)

@login_required
def order_confirmation(request):
    # Retrieve the most recent order for the current user
    recent_order = Checkout.objects.filter(user=request.user).order_by('-created_at').first()

    # Check if a recent order was found
    if recent_order:
        items = OrderItem.objects.filter(order=recent_order)
        total_cost = recent_order.order_total
    else:
        items = []
        total_cost = None

    context = {
        'order': recent_order,
        'items': items,
        'total_cost': total_cost,
    }
    return render(request, 'order_confirmation.html', context)





@login_required
def order_list(request):
    orders = Checkout.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'order_list.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Checkout, id=order_id, user=request.user)
    order_items = OrderItem.objects.filter(order=order)
    return render(request, 'order_detail.html', {'order': order, 'order_items': order_items})

