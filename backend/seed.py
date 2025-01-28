#!/usr/bin/env python3

from app import app
from models import db, User, Product, Order, OrderProduct

with app.app_context():

    # Delete existing data to avoid duplicates
    print("Deleting data...")
    OrderProduct.query.delete()
    Order.query.delete()
    Product.query.delete()
    User.query.delete()

    # Create users
    print("Creating users...")
    user1 = User(name="Alice", email="alice@example.com", budget=5000.0)
    user2 = User(name="Bob", email="bob@example.com", budget=3000.0)
    user3 = User(name="Charlie", email="charlie@example.com", budget=7000.0)
    users = [user1, user2, user3]

    # Create products
    print("Creating products...")
    sofa = Product(name="Luxury Sofa", description="A comfortable luxury sofa.", price=1500.0, category="Sofa", image_url="https://example.com/sofa.jpg")
    bed = Product(name="King Size Bed", description="A spacious and stylish bed.", price=2000.0, category="Bed", image_url="https://example.com/bed.jpg")
    chair = Product(name="Ergonomic Chair", description="Perfect for work and study.", price=500.0, category="Chair", image_url="https://example.com/chair.jpg")
    products = [sofa, bed, chair]

    # Create orders
    print("Creating orders...")
    order1 = Order(user=user1)
    order2 = Order(user=user2)
    order3 = Order(user=user3)
    orders = [order1, order2, order3]

    # Create order products (association table with quantity)
    print("Creating order products...")
    order_product1 = OrderProduct(order=order1, product=sofa, quantity=1, special_request="Deliver in the morning")
    order_product2 = OrderProduct(order=order2, product=bed, quantity=1, special_request="Assemble on-site")
    order_product3 = OrderProduct(order=order3, product=chair, quantity=2, special_request="Gift wrap each chair")
    order_products = [order_product1, order_product2, order_product3]

    # Add all to session and commit
    db.session.add_all(users)
    db.session.add_all(products)
    db.session.add_all(orders)
    db.session.add_all(order_products)
    db.session.commit()

    print("Seeding done!")
