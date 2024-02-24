import socket
import logging
import pickle
from common import ADDR
from classesdz5 import *

logger = logging.getLogger(__name__)
logging.basicConfig()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c = s.bind(ADDR)
s.listen(5)

s.setblocking(False)
s.settimeout(1)

while True:
    try:
        client_socket = s.accept()
    except TimeoutError:
        continue
    client, (addr, port) = client_socket
    logger.warning(f"{addr} connected from port {port}")

    data = [regular_polyhedron, cube, tetrahedron, octahedron]

    client.send(pickle.dumps(data, protocol=pickle.DEFAULT_PROTOCOL))
    client.close()
