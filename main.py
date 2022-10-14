"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
import os
from flask import Flask, redirect, request, render_template

import stripe
# This is your test secret API key.
stripe.api_key = 'sk_test_51LnQtrGbuqleXZx6wfUJ704aZjcndAjRz3gnUxmwour6PH42PeKwZxvBiRoMIQ8Fo8DiaSxyERzibJqlTVIcOQ7l00JnpjA7Y4'

app = Flask(__name__)

YOUR_DOMAIN = 'http://127.0.0.1:5000/'


@app.route('/create-checkout-session', methods=['GET', 'POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1LnSeiGbuqleXZx6TFsRrfvM',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + 'success.html',
            cancel_url=YOUR_DOMAIN + 'cancel.html',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/checkout')
def checkout():
    return render_template('checkout.html')


if __name__ == '__main__':
    app.run()