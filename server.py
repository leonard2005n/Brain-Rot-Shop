from flask import Flask, render_template, request, redirect, session, url_for, flash
import os, json
from products import products

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/cart')
def cart():
	cart_items = session.get('cart', {})
	return render_template('cart.html', cart_items=cart_items, products=products)

@app.route('/cart/increment')
def increment_item():
	product_id = request.args.get('id')
	cart = session.get('cart', {})
	if product_id in cart:
		cart[product_id] += 1
	session['cart'] = cart
	session.modified = True
	return redirect(url_for('cart'))

@app.route('/cart/decrement')
def decrement_item():
	product_id = request.args.get('id')
	cart = session.get('cart', {})
	if product_id in cart:
		cart[product_id] -= 1
		if cart[product_id] <= 0:
			cart.pop(product_id)
	session['cart'] = cart
	session.modified = True
	return redirect(url_for('cart'))

@app.route('/cart/add-item')
def add_to_cart():
    product_id = request.args.get('id')
    if not product_id:
        flash("Invalid product ID", "danger")
        return redirect(url_for('index'))

    cart = session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + 1
    session['cart'] = cart
    session.modified = True
    flash("Item added to cart!", "success")
    return redirect(url_for('index'))

@app.route('/cart/remove-item')
def remove_from_cart():
    product_id = request.args.get('id')
    cart = session.get('cart', {})
    if product_id in cart:
        cart.pop(product_id)
    session['cart'] = cart
    return redirect(url_for('cart'))

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        order = {
            "full_name": request.form['full_name'],
            "email": request.form['email'],
            "phone": request.form['phone'],
            "address": request.form['address'],
            "payment_method": request.form['payment_method'],
            "cart": session.get('cart', {})
        }
        os.makedirs('submitted-data', exist_ok=True)
        with open(f'submitted-data/order_{order["email"]}.json', 'w') as f:
            json.dump(order, f, indent=2)
        print(order)  # Console debug
        session['cart'] = {}  # Clear cart after order
        return 'Order placed successfully!'
    return render_template('checkout.html', cart=session.get('cart', {}), products=products)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
