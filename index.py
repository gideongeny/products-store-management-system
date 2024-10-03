import json
import os


USER_FILE = 'users.json'
PRODUCT_FILE = 'products.json'


def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []

def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


class Product:
    def __init__(self, title, description, variations, price, quantity):
        self.title = title
        self.description = description
        self.variations = variations 
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.title} - {self.description} - {self.price}$ (Stock: {self.quantity})'

class Variation:
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def __str__(self):
        return f'Size: {self.size}, Color: {self.color}'

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cart = Cart()

    def add_to_cart(self, product, quantity):
        self.cart.add_product(product, quantity)

class ProductStore:
    def __init__(self):
        self.products = load_data(PRODUCT_FILE)

    def add_product(self, product):
        self.products.append(product)
        self.save_products()

    def list_products(self):
        for product in self.products:
            print(product)

    def save_products(self):
        products_to_save = []
        for product in self.products:
            product_dict = {
                'title': product.title,
                'description': product.description,
                'variations': [{'size': v.size, 'color': v.color} for v in product.variations],
                'price': product.price,
                'quantity': product.quantity
            }
            products_to_save.append(product_dict)
        save_data(PRODUCT_FILE, products_to_save)

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        self.items.append((product, quantity))

    def view_cart(self):
        for item, quantity in self.items:
            print(f'{item.title}: {quantity} x {item.price}$ = {quantity * item.price}$')

    def checkout(self, product_store):
        total = 0
        for product, quantity in self.items:
            if product.quantity >= quantity:
                product.quantity -= quantity
                total += quantity * product.price
            else:
                print(f'Not enough stock for {product.title}')
        product_store.save_products()
        return total

# User Account Management
def register_user():
    users = load_data(USER_FILE)
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")

    for user in users:
        if user['username'] == username:
            print("Username already exists!")
            return

    users.append({'username': username, 'password': password})
    save_data(USER_FILE, users)
    print("User registered successfully!")

def login():
    users = load_data(USER_FILE)
    username = input("Enter username: ")
    password = input("Enter password: ")

    for user in users:
        if user['username'] == username and user['password'] == password:
            print("Login successful!")
            return User(username, password)

    print("Invalid credentials.")
    return None


def main():
    product_store = ProductStore()

    while True:
        print("\n--- Online Product Store ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            user = login()
            if user:
                while True:
                    print("\n--- User Menu ---")
                    print("1. Browse Products")
                    print("2. Add Product to Cart")
                    print("3. View Cart")
                    print("4. Checkout")
                    print("5. Logout")
                    user_choice = input("Select an option: ")

                    if user_choice == '1':
                        product_store.list_products()
                    elif user_choice == '2':
                        product_store.list_products()
                        product_title = input("Enter the product title to add to cart: ")
                        for product in product_store.products:
                            if product.title == product_title:
                                quantity = int(input("Enter quantity: "))
                                user.add_to_cart(product, quantity)
                                print(f'{product.title} added to cart.')
                                break
                        else:
                            print("Product not found.")
                    elif user_choice == '3':
                        user.cart.view_cart()
                    elif user_choice == '4':
                        total = user.cart.checkout(product_store)
                        print(f"Total amount: {total}$")
                    elif user_choice == '5':
                        break
        elif choice == '3':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
