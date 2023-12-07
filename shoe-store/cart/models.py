from django.db import models
from django.utils.timezone import now

class Cart(models.Model):
    user = models.OneToOneField(
        "users.User",
        related_name="cart",
        on_delete=models.CASCADE,
        null=True,  
        blank=True, 
        unique=True,
        verbose_name="user",
        help_text="The user to whom this shopping cart belongs"
    )

    session_key = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        verbose_name="session key",
        help_text="Session key for anonymous user carts"
    )
    
    created_at = models.DateTimeField(
        default=now,
        verbose_name="created at",
        help_text="The timestamp indicating when the shopping cart was created"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="updated at",
        help_text="The timestamp indicating when the shopping cart was last updated"
    )
    is_active = models.BooleanField(default=True, help_text="Indicates if the cart is active")


    def __str__(self):
        if self.user:
            return f"Cart of {self.user.username}"
        else:
            return f"Cart with session key {self.session_key}" 
        
    def get_total_price(self):
        return sum(item.sub_total() for item in self.cart_items.all())

    def __str__(self):
        return f"Cart of {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        related_name="cart_items",
        on_delete=models.CASCADE,
        null=True,  
        blank=True,  
        verbose_name="shopping cart",
        help_text="The shopping cart to which this item belongs"
    )
    session_key = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        verbose_name="session key",
        help_text="Session key for anonymous user carts"
    )

    product = models.ForeignKey(
        "products.ProductModel",
        related_name="cart_items",
        on_delete=models.CASCADE,
        verbose_name="product",
        help_text="The product included in this cart item"
    )
    quantity = models.IntegerField(
        default=1,
        verbose_name="quantity",
        help_text="The quantity of the products in this cart item"
    )


    def __str__(self):
        if self.user:
            return f"Cart of {self.user.username}"
        else:
            return f"Cart with session key {self.session_key}" 
        

    def sub_total(self):
        return self.product.price * self.quantity

    def is_product_available(self):
        return self.quantity <= self.product.stock

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

class Checkout(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
    ]

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        verbose_name="user",
        help_text="The user who is checking out"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="created at",
        help_text="The timestamp indicating when the checkout was created"
    )
    order_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="order total",
        help_text="Total cost of the order"
    )
    payment_status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        default='Pending',
        verbose_name="payment status",
        help_text="Status of the payment"
    )
    transaction_id = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="transaction id",
        help_text="Transaction ID for the payment"
    )

    
    payment_option = models.CharField(
        max_length=100,
        choices=[('credit_card', 'Credit Card'), ('visa', 'Visa'), ('debit_card', 'Debit Card')],
        default='credit_card',
        verbose_name="payment option",
    )
    delivery_address = models.TextField(
        null=True,
       
    )

    def __str__(self):
        return f"Checkout by {self.user.username} - Total: {self.order_total}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Checkout,
        related_name='order_items',
        on_delete=models.CASCADE,
        verbose_name="order",
        help_text="The checkout order to which this item belongs"
    )
    product = models.ForeignKey(
        "products.ProductModel",
        on_delete=models.CASCADE,
        verbose_name="product",
        help_text="The product included in this order item"
    )
    quantity = models.PositiveIntegerField(
        verbose_name="quantity",
        help_text="The quantity of the product in this order item"
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="price",
        help_text="Price of the product"
    )
    cart_item = models.ForeignKey(
        CartItem,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="cart item",
        help_text="The cart item that was ordered"
    )

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in order {self.order.id}"
