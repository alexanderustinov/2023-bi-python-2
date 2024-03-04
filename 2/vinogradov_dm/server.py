import socket
import logging
import pickle

from common import ADDR
from dz import *
logger = logging.getLogger(__name__)
logging.basicConfig()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c = s.bind(ADDR)
s.listen(5)

s.setblocking(False)
s.settimeout(1)

while True:
    try:
        clientsocket, addr = s.accept()
    except TimeoutError:
        continue
    client, (addr, port) = clientsocket
    logger.warning(f"{addr} connected from port {port}")

    data = {Fr, Ci, B}

    client.send(pickle.dumps(data, protocol=pickle.HIGHEST_PROTOCOL))

    client.close()
