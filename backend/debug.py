from app import app, db
from models import User, Product, Order

with app.app_context():
    print("Users:", User.query.all())
    print("Products:", Product.query.all())
    print("Orders:", Order.query.all())
