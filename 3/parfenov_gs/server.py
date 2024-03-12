import asyncio
import logging
import pickle

from classes import *
from common import AD, DR

logger = logging.getLogger(__name__)
logging.basicConfig()

async def server_feetler(reader, writer):
    logger.info("connection is established")
    data = [name_and_element, vision_archon, character]
    writer.write(pickle.dumps(data, protocol=pickle.HIGHEST_PROTOCOL))
    await writer.drain()
    logger.info('sent')


async def main_server():
    print(AD, DR)
    server = await asyncio.start_server(server_feetler, AD, DR)

    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(main_server())
    
    



