import logging
import pickle
from common import ADDR
import asyncio
from classesdz5 import regular_polyhedron, cube, tetrahedron, octahedron

logger = logging.getLogger(__name__)
logging.basicConfig()

async def server_handler(reader, writer):
    logger.info('Connected')
    data = [regular_polyhedron, cube, tetrahedron, octahedron]
    writer.write(pickle.dumps(data, protocol=pickle.HIGHEST_PROTOCOL))
    await writer.drain()
    logger.info('Sent')


async def main_server():
    print(ADDR[0], ADDR[1])
    server = await asyncio.start_server(server_handler, ADDR[0], ADDR[1])

    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(main_server())
