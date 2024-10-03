# Online Product Store Management System

This system is a command-line-based application allowing users to browse products, add them to their cart, and proceed to checkout.

## Features:
- **Account Creation and Login**: Users can create accounts and login to access the store.
- **Product Browsing and Cart Management**: Users can browse available products, add items to their cart, view cart details, and remove items.
- **JSON-Based Storage**: Both user accounts and products are stored in JSON files for persistence across sessions.
- **Checkout Functionality**: Users can proceed to checkout, which updates the product stock and provides the total purchase amount.
  
## Procedures:

1. **Create an Account**: 
   - When starting the system, select the option to create a new account.
   - Enter a username and password which will be stored in the `users.json` file.
  
2. **Login**: 
   - After creating an account, you can log in using the stored credentials.
  
3. **Browse Products**: 
   - After logging in, you can browse available products, which are stored in the `products.json` file.
  
4. **Add to Cart**: 
   - Select products and the desired quantity to add them to your shopping cart.
  
5. **View Cart**: 
   - View the items you’ve added to your cart, including the total price.
  
6. **Checkout**: 
   - Proceed to checkout, confirm the purchase, and the quantities of purchased products will be deducted from the product store.

## Requirements:

- Python 3.x
- JSON files for storing product and user data (`users.json`, `products.json`).

## Running the Program:

1. Ensure `users.json` and `products.json` files exist in the same directory as the script.
2. Execute the script using Python:
   ```bash
   python product_store.py
   ```

## JSON Structure:

### Users:
```json
[
    {
        "username": "example_user",
        "password": "example_password"
    }
]
```

### Products:
```json
[
    {
        "title": "Product 1",
        "description": "Description of product 1",
        "variations": [
            {"size": "M", "color": "Red"}
        ],
        "price": 20.0,
        "quantity": 50
    }
]
