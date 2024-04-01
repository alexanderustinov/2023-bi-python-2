import socket
import logging
import pickle

from classes import DNA
from common import ADDR

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(ADDR)
s.listen(5)

s.setblocking(False)
s.settimeout(1)

while True:
    try:
        client_socket, addr = s.accept()
    except socket.timeout:
        continue

    logger.warning(f"{addr[0]} connected from port {addr[1]}")

    dna_sample1 = DNA("ATCG")
    dna_sample2 = DNA("GGGAATTC")
    dna_sample3 = DNA("CCCGGG")

    data_to_send = [dna_sample1, dna_sample2, dna_sample3]
    serialized_data = pickle.dumps(data_to_send, protocol=pickle.HIGHEST_PROTOCOL)

    client_socket.send(serialized_data)

    client_socket.close()
