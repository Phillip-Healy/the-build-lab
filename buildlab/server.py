#! /usr/bin/env python3.6

"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""
import os
from flask import Flask, redirect, request

import stripe
# This is a sample test API key. Sign in to see examples pre-filled with your key.
stripe.api_key = 'sk_test_51JvT9mBRo6elGpC9LaoqsFUQPdNWoFOToUs7rqdFqFa74Aw1qBE157nBD12gc9TjOfdPiv3ettpOARud0cK55EOd00aiMvJJis'

app = Flask(__name__,
            static_url_path='',
            static_folder='public')

YOUR_DOMAIN = 'http://localhost:4242'


@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (e.g. pr_1234) of the product you want to sell
                    'price': '{{prod_KaefI3Mwg5gVIg}}',
                    'quantity': 1,
                },
            ],
            payment_method_types=[
              'card',
            ],
            mode='payment',
            success_url= {% url '' %} + '/success.html',
            cancel_url= {% url '' %} + '/cancel.html',
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)

if __name__ == '__main__':
    app.run(port=4242)