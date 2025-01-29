
#!/usr/bin/env python3
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_restful import Api
from models import db, User, Product, Order, OrderProduct
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)


@app.route("/")
def index():
    return "<h1>E-Commerce Furniture Store</h1>"


# User routes
@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        users = User.query.all()
        users_dict = [user.to_dict(only=("id", "name", "email", "budget")) for user in users]
        return jsonify(users_dict), 200

    elif request.method == "POST":
        data = request.get_json()
        try:
            user = User(
                name=data["name"],
                email=data["email"],
                budget=data["budget"]
            )
            db.session.add(user)
            db.session.commit()
            return jsonify(user.to_dict()), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400


# Product routes
@app.route("/products", methods=["GET", "POST"])
def products():
    if request.method == "GET":
        products = Product.query.all()
        products_dict = [product.to_dict(only=("id", "name", "description", "price", "category", "image_url")) for product in products]
        return jsonify(products_dict), 200

    elif request.method == "POST":
        data = request.get_json()
        try:
            product = Product(
                name=data["name"],
                description=data["description"],
                price=data["price"],
                category=data["category"],
                image_url=data["image_url"]
            )
            db.session.add(product)
            db.session.commit()
            return jsonify(product.to_dict()), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400


# Order routes
@app.route("/orders", methods=["GET", "POST"])
def orders():
    if request.method == "GET":
        orders = Order.query.all()
        orders_dict = [order.to_dict(only=("id", "user_id", "total_cost", "order_products")) for order in orders]
        return jsonify(orders_dict), 200

    elif request.method == "POST":
        data = request.get_json()
        try:
            order = Order(
                user_id=data["user_id"],
                total_cost=data["total_cost"]
            )
            db.session.add(order)
            db.session.commit()
            return jsonify(order.to_dict()), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400


# OrderProduct routes
@app.route("/order_products", methods=["POST"])
def add_order_product():
    data = request.get_json()
    try:
        order_product = OrderProduct(
            order_id=data["order_id"],
            product_id=data["product_id"],
            quantity=data["quantity"],
            special_request=data["special_request"]
        )
        db.session.add(order_product)
        db.session.commit()
        return jsonify(order_product.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(port=5555, debug=True)