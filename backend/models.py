from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class User(BaseModel):
    __tablename__ = "users"

    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    budget = db.Column(db.Float, nullable=False, default=0.0)
    orders = db.relationship('Order', backref='user', lazy=True)

    def __repr__(self):
        return f"<User {self.id} - {self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "budget": self.budget,
            "orders": [order.to_dict() for order in self.orders]
        }

class Order(BaseModel):
    __tablename__ = "orders"

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    total_cost = db.Column(db.Float, nullable=False, default=0.0)
    order_products = db.relationship('OrderProduct', backref='order', lazy=True)

    def __repr__(self):
        return f"<Order {self.id} by User {self.user_id}>"

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "total_cost": self.total_cost,
            "products": [op.to_dict() for op in self.order_products]
        }

class OrderProduct(BaseModel):
    __tablename__ = "order_products"

    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    special_request = db.Column(db.String(255), nullable=True)
    product = db.relationship('Product', backref='order_products', lazy=True)

    def __repr__(self):
        return f"<OrderProduct {self.id} - Order {self.order_id} - Product {self.product_id}>"

    def to_dict(self):
        return {
            "id": self.id,
            "order_id": self.order_id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "special_request": self.special_request,
            "product": self.product.to_dict()
        }

class Product(BaseModel):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(2048), nullable=False)
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "category": self.category,
            "image_url": self.image_url,
        }