from app import app, db
from models import User, Product, Order

with app.app_context():
    db.drop_all()
    db.create_all()

    # Sample Users
    user1 = User(name="Alice", email="alice@example.com", budget=5000.00)
    user2 = User(name="Bob", email="bob@example.com", budget=3000.00)

    # Sample Products
    product1 = Product(name="Sofa", description="Comfortable sofa", price=1000.00, category="Living Room", image_url="sofa.jpg")
    product2 = Product(name="Bed", description="King size bed", price=1500.00, category="Bedroom", image_url="bed.jpg")

    # Sample Orders
    order1 = Order(user_id=1, product_id=1, quantity=1, special_request="Add extra cushions")
    order2 = Order(user_id=2, product_id=2, quantity=1, special_request="Deliver by weekend")

    db.session.add_all([user1, user2, product1, product2, order1, order2])
    db.session.commit()

    print("Database seeded!")
