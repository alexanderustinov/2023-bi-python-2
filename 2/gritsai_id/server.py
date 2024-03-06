import socket
import logging
import pickle

from classes import Laundry, Clothing
from common import ADDR

logger = logging.getLogger(__name__)
logging.basicConfig()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)
s.listen(5)

while True:
    client_socket, addr = s.accept()
    logger.warning(f"{addr} connected ")

    laundry = Laundry()
    socks = Clothing("Носки", "M")
    shirt = Clothing("Рубашка", "L")

    laundry.add_item(socks)
    laundry.add_item(shirt)
    
    client_socket.send(pickle.dumps(laundry))
    client_socket.close()
