import asyncio
import logging
import pickle
from common import ADDR

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

async def receive_dna_samples():
    reader, writer = await asyncio.open_connection(*ADDR)
    logger.info(f"Connected to server at {ADDR}")

    serialized_data = await reader.read(4096)
    dna_samples = pickle.loads(serialized_data)

    for dna in dna_samples:
        logger.info(f"Received DNA sequence: {dna.sequence}")

    writer.close()
    await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(receive_dna_samples())
