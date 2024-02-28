# main_page.py
from flask import Flask, render_template, request, redirect, url_for
from order_model import db, Order

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # link database w orders
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/") # main menu is the default page
def default():
    return render_template("Main_Page.html")

@app.route('/order_summary', methods=['POST']) # order summary page
def order_summary():
    # get form data
    customer_name = request.form.get('customer-name')
    order_details = request.form.get('order-details')

    # create a new order object
    new_order = Order(customer_name=customer_name, orders=order_details, order_number=123)

    # add the new order into the database
    db.session.add(new_order)
    db.session.commit()
    return render_template('order_summary.html', customer_name=customer_name, items=order_details.split('\n'))

@app.route('/kitchen/') # kitchen database
def kitchen():
    # get all orders from the database
    orders = Order.query.all()

    # convert each Order object into a JSON object using toJSON method i wrote
    orders_json = [order.toJSON() for order in orders]

    # render the kitchen.html file and pass the JSON object array
    return render_template('kitchen.html', orders_json=orders_json)

@app.route('/delete/<int:id>')
def delete_order(id):
    # get the order from the database
    order = Order.query.get(id)

    # check if the order exists (bc otherwise you shouldn't be able to delete)
    if order:
        # delete the order from the database
        db.session.delete(order)
        db.session.commit()

    # redirect to the kitchen page
    return redirect(url_for('kitchen'))

if __name__ == '__main__':
    app.run(debug=True)