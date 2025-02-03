from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS
from models import db, User, Product, Order, OrderProduct
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get("DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

CORS(app)
db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)

@app.route("/", methods=["GET"])  
def index():
    return "<h1>E-Commerce Furniture Store</h1>", 200

# User Routes
@app.route("/users", methods=["GET", "POST"]) 
def users():
    if request.method == "GET":
        users = User.query.all()
        return jsonify([user.to_dict() for user in users]), 200
    
    if request.method == "POST":
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

@app.route("/users/<int:user_id>", methods=["PATCH", "DELETE"]) 
def user_detail(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    if request.method == "PATCH":
        data = request.get_json()
        user.budget = data.get("budget", user.budget)
        db.session.commit()
        return jsonify(user.to_dict()), 200
    
    if request.method == "DELETE":
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted"}), 200

# Product Routes
@app.route("/products", methods=["GET", "POST"])  
def products():
    if request.method == "GET":
        products = Product.query.all()
        return jsonify([product.to_dict() for product in products]), 200
    
    if request.method == "POST":
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

@app.route("/products/<int:product_id>", methods=["PATCH", "DELETE"])  
def product_detail(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    if request.method == "PATCH":
        data = request.get_json()
        for key, value in data.items():
            setattr(product, key, value)
        db.session.commit()
        return jsonify(product.to_dict()), 200
    
    if request.method == "DELETE":
        db.session.delete(product)
        db.session.commit()
        return jsonify({"message": "Product deleted"}), 200

# Order Routes
@app.route("/orders", methods=["GET", "POST"])  
def orders():
    if request.method == "GET":
        orders = Order.query.all()
        return jsonify([order.to_dict() for order in orders]), 200
    
    if request.method == "POST":
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

@app.route("/orders/<int:order_id>", methods=["DELETE"])
def delete_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    
    db.session.delete(order)
    db.session.commit()
    return jsonify({"message": "Order deleted"}), 200

# Order Product Routes
@app.route("/order_products", methods=["POST"]) 
def add_order_product():
    data = request.get_json()
    try:
        order_product = OrderProduct(
            order_id=data["order_id"],
            product_id=data["product_id"],
            quantity=data["quantity"],
            special_request=data.get("special_request")
        )
        db.session.add(order_product)
        db.session.commit()
        
        # Update the order total cost
        order = Order.query.get(data["order_id"])
        order.total_cost += order_product.product.price * order_product.quantity
        db.session.commit()
        
        return jsonify(order.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/order_products/<int:order_id>", methods=["GET"])
def get_order_products(order_id):
    order_products = OrderProduct.query.filter_by(order_id=order_id).all()
    return jsonify([order_product.to_dict() for order_product in order_products]), 200

@app.route("/order_products/<int:order_id>/<int:product_id>", methods=["DELETE"])  
def delete_order_product(order_id, product_id):
    order_product = OrderProduct.query.filter_by(order_id=order_id, product_id=product_id).first()
    if not order_product:
        return jsonify({"error": "Order product not found"}), 404
    
    db.session.delete(order_product)
    db.session.commit()
    return jsonify({"message": "Order product deleted"}), 200

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5555)