import socket
import logging
import pickle
import random

from common import ADDR
from classes_5 import Product, Customer

logger = logging.getLogger(__name__)
logging.basicConfig()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)
s.listen(5)
print("Сервера запущен")
while True:
    client_socket, addr = s.accept()
    logger.warning(f"{addr} connected")

    product1 = Product("Футболка", 500)
    product2 = Product("Джинсы", 1000)
    
    quantity = random.randint(1, 5)
    discount = random.uniform(0, 0.2)

    customer = Customer("Иван")
    customer.add_to_cart(product1, quantity)
    customer.add_to_cart(product2, quantity)

    customer_data = pickle.dumps(customer)

    client_socket.send(customer_data)
    client_socket.close()
