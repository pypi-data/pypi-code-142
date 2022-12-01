import requests
import json
import os

URL = os.getenv("QE_API_SERVER")

def login_user(server, login_id, login_password):
    response = requests.request("POST", f"http://{URL}/api/login_user/", data={
        'server': server,
        'username': login_id,
        'password': login_password
    })
    return json.loads(response.text)

def cart(server, restaurant, session):
    response = requests.request("GET",
                                f"http://{URL}/api/cart?server={server}&restaurant={restaurant}&session={session}")
    return json.loads(response.text)

def cart_submit(server, lat, lng, restaurant, session, delivery_fee, full_price, email, phone):
    response = requests.request("POST", f"http://{URL}/api/cart_submit/", data={
        'server': server,
        'lat': lat,
        'lng': lng,
        'restaurant': restaurant,
        'session': session,
        'delivery_fee': delivery_fee,
        'full_price': full_price,
        'email': email,
        'phone': phone
    })
    return json.loads(response.text)

def complete_order(server, username, password, restaurant, email, phone):
    session_id = login_user(server, username, password)['sessionid']
    cart_data = cart(server,restaurant, session_id)
    order_data = cart_submit(server,cart_data['lat'], cart_data['lng'], restaurant, session_id, cart_data['delivery_fee'], cart_data['full_price'], email, phone)
    return order_data['order_number']