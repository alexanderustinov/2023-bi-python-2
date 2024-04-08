import logging
import pickle
import asyncio
from classes import Tee
from common import ADDR


logger = logging.getLogger(__name__)
logging.basicConfig()

async def handle_client(reader, writer):
    logger.warning("connected")
    tee = Tee('green', 10)
    

    data = pickle.dumps(tee)
    writer.write(data)
    await writer.drain()
    print('OK')


async def main():
    server = await asyncio.start_server(
        handle_client, ADDR[0], ADDR[1])

    #addr = server.sockets[0].getsockname()
    #print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(main())
