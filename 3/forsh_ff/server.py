import logging
import pickle
import asyncio

from classes import *
from common import HOST, PORT

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


async def server_handler(reader, writer):
    logger.info("successful connected")
    data = [RegularPolygon, Quadrilateral, Square, Triangle]
    writer.write(pickle.dumps(data, protocol=pickle.HIGHEST_PROTOCOL))
    await writer.drain()
    logger.info('successful sending')


async def main_server():
    print(HOST, PORT)
    server = await asyncio.start_server(server_handler, HOST, PORT)

    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(main_server())
