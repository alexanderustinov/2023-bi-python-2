import socket
import logging
import pickle
from common import ADDR 

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def receive_dna_samples():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(ADDR)
        logger.info(f"Connected to server at {ADDR}")

        serialized_data = s.recv(4096)
        dna_samples = pickle.loads(serialized_data)

        for dna in dna_samples:
            logger.info(f"Received DNA sequence: {dna.sequence}")

receive_dna_samples()