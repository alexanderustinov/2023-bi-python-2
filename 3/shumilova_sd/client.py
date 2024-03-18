import pickle
import asyncio

from common import ADDR

async def client_func():
    reader, writer = await asyncio.open_connection(ADDR[0], ADDR[1])
    response = await reader.read(1024)
    data = pickle.loads(response)
    for i in data:
        print(f"got {i}" )
    writer.close()


if __name__ == '__main__':
    asyncio.run(client_func())
