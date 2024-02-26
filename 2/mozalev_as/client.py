import socket
import json

from common import ADDR
from classes_5 import Customer, Product

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDR)
data = s.recv(4096).decode()


customer_data = json.loads(data)
customer = Customer(customer_data['name'])


for item_data in customer_data['cart']:
    product = Product(item_data['name'], item_data['price'])
    customer.add_to_cart(product, item_data['quantity'])


customer.view_cart()
s.close()
