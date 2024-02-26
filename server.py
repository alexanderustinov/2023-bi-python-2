import socket
import logging
import pickle

from common import ADDR
from dz import *
logger = logging.getLogger(name)
logging.basicConfig()

s = socket.socket(socket.AFINET, socket.SOCKSTREAM)

s.bind(ADDR)
s.listen(5)

s.setblocking(False)
s.settimeout(1)

while True:
    try:
        clientsocket, addr = s.accept()
    except socket.timeout:
        continue
    client, (addr, port) = clientsocket
    logger.warning(f"{addr} connected from port {port}")

    data = {Fr, Ci, B}

    client.send(pickle.dumps(data))

    client.close()