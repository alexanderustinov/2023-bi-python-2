import asyncio
import logging
import pickle

from classes import DNA
from common import ADDR

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


async def handle_client(reader, writer):
    dna_sample1 = DNA("ATCG")
    dna_sample2 = DNA("GGGAATTC")
    dna_sample3 = DNA("CCCGGG")

    data_to_send = [dna_sample1, dna_sample2, dna_sample3]
    serialized_data = pickle.dumps(data_to_send, protocol=pickle.HIGHEST_PROTOCOL)

    writer.write(serialized_data)
    await writer.drain()
    writer.close()
    await writer.wait_closed()


async def main():
    server = await asyncio.start_server(handle_client, *ADDR)
    addr = server.sockets[0].getsockname()
    logger.info(f"Serving on {addr}")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
