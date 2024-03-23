import asyncio
import logging
import pickle

from common import ADDR
from classes import Laundry, Clothing

logger = logging.getLogger(__name__)
logging.basicConfig()


async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    logger.warning(f"{addr} connected ")

    laundry = Laundry()
    socks = Clothing("Носки", "M")
    shirt = Clothing("Рубашка", "L")

    laundry.add_item(socks)
    laundry.add_item(shirt)

    data = pickle.dumps(laundry)
    writer.write(data)
    await writer.drain()

    writer.close()


async def main():
    server = await asyncio.start_server(
        handle_client, ADDR[0], ADDR[1])

    async with server:
        await server.serve_forever()


asyncio.run(main())
