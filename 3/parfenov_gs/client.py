import asyncio
import pickle

from common import AD, DR

async def client_function():
    reader, writer = await asyncio.open_connection(AD, DR)
    answer = await reader.read(1024)
    data = pickle.loads(answer)
    for i in data:
        print(f"got {i}" )
    writer.close()


if __name__ == '__main__':
    asyncio.run(client_function())