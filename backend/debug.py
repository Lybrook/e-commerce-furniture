#!/usr/bin/env python3

from app import app
from models import db, User, Product, Order, OrderProduct

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)