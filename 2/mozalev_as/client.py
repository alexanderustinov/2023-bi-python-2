import socket
import pickle

from common import ADDR
from classes_5 import Customer, Product, ShoppingCartItem

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDR)
data = s.recv(4096)

customer = pickle.loads(data)

customer.view_cart()
s.close()
