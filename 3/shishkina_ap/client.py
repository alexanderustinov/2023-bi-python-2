import pickle
import asyncio

from common import ADDR

async def main():
    reader, writer = await asyncio.open_connection(*ADDR)
    data = await reader.read(4096)
    Tee = pickle.loads(data)
    print(Tee)
    Tee.tea_party()
    writer.close()


if __name__ == '__main__':
    asyncio.run(main())