from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)

db = SQLAlchemy(metadata=metadata)

class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    budget = db.Column(db.Float, nullable=False)

    orders = db.relationship('Order', back_populates='user', cascade='all, delete-orphan')

    serialize_rules = ('-orders.user',)

    def __repr__(self):
        return f"<User {self.name}, {self.email}>"


class Product(db.Model, SerializerMixin):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String)

    order_products = db.relationship('OrderProduct', back_populates='product', cascade='all, delete-orphan')

    serialize_rules = ('-order_products.product',)

    @validates('price')
    def validate_price(self, key, price):
        if price <= 0:
            raise ValueError("Price must be greater than 0")
        return price

    def __repr__(self):
        return f"<Product {self.name}, {self.price}>"


class Order(db.Model, SerializerMixin):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='orders')
    order_products = db.relationship('OrderProduct', back_populates='order', cascade='all, delete-orphan')

    products = association_proxy('order_products', 'product',
                                  creator=lambda product_obj: OrderProduct(product=product_obj))

    serialize_rules = ('-order_products.order', '-user.orders')

    def __repr__(self):
        return f"<Order {self.id} by User {self.user_id}>"


class OrderProduct(db.Model, SerializerMixin):
    __tablename__ = "order_products"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    special_request = db.Column(db.String)

    order = db.relationship('Order', back_populates='order_products')
    product = db.relationship('Product', back_populates='order_products')

    serialize_rules = ('-order.order_products', '-product.order_products')

    @validates('quantity')
    def validate_quantity(self, key, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        return quantity

    def __repr__(self):
        return f"<OrderProduct {self.quantity} of Product {self.product_id} in Order {self.order_id}>"
