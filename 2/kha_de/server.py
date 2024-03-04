import socket
import logging
import pickle

from penguin import *
from common import AAA

logger = logging.getLogger(__name__)
logging.basicConfig()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c = s.bind(AAA)
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

    if port % 2 == 0:
        bird = Penguin('Emperor Penguin', '130', '25', '35', '40')
    else:
        bird = Penguin('Rockhopper Penguin', '60', '25', '2', '3')
    client.send(pickle.dumps(bird))

    client.close()