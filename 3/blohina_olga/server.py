import asyncio
import pickle
import logging
from old_5 import Lang, Proc, Nproc
from common import ADDR

logger = logging.getLogger(__name__)
logging.basicConfig(level = logging.INFO)

async def Server(reader, writer):
    logger.info('Connected')
    data = [Lang, Proc, Nproc]
    writer.write(pickle.dumps(data, protocol=pickle.HIGHEST_PROTOCOL))
    await writer.drain()
    logger.info('Sent')

async def Main_Server():
    print(ADDR[0], ADDR[1])
    server = await asyncio.start_server(Server, ADDR[0], ADDR[1])

    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(Main_Server())
