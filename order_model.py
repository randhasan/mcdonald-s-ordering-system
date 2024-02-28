# order_model.py
from datetime import datetime # need to get the date and time
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # SQLAlchemy instance

class Order(db.Model): # model for orders
    # make database columns for Order class
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    orders = db.Column(db.String(500), nullable=False)
    order_number = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow) # date and time the order was created.  default time is current UTC

    # convert Order to JSON format
    def toJSON(self):
        return {
            "id": self.id,
            "customer_name": self.customer_name,
            "orders": self.orders,
            "order_number": self.order_number,
            "date_created": self.date_created.strftime("%Y-%m-%d %H:%M:%S") # makes date and time readable
        }
