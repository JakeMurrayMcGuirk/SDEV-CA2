function addToWishlist(productId) {
    // Makes an AJAX request to add the product to the wishlist
    fetch(`/wishlist/add/${productId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}'  // Add your CSRF token here
        },
        body: JSON.stringify({ product_id: productId })
    })
    .then(response => {
        if (response.ok) {
            // Notify the user that the product was added to the wishlist
            alert('Product added to the wishlist!');
        } else {
            // Handle error responses
            console.error('Error adding product to wishlist');
        }
    })
    .catch(error => {
        console.error('Error adding product to wishlist:', error);
    });
}

function addToCart(productId) {
    // AJAX request to add product to cart
    // Example using fetch API
    fetch(`/cart/add/${productId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            // Add any necessary headers or authentication tokens
        },
        body: JSON.stringify({ quantity: 1 }), // You can adjust the quantity as needed
    })
    .then(response => {
        // Handle the response accordingly (e.g., update UI, show message)
        console.log('Product added to cart:', response);
    })
    .catch(error => {
        // Handle any errors that occurred during the fetch
        console.error('Error adding product to cart:', error);
    });
}
