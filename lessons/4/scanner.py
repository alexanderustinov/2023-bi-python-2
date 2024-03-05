import asyncio

class TcpConnector(asyncio.Transport):
    def connection_made(self, transport):
        transport.close()
    def connection_lost(self, exc):
        pass

# не больше 50 подключений одновременно
semaphore = asyncio.Semaphore(50)

async def try_connect(ip, port):
    loop = asyncio.get_running_loop()
    try:
        await semaphore.acquire()
        await asyncio.wait_for(loop.create_connection(TcpConnector, ip, port), 0.1)
    except Exception as e:
        pass
    else:
        return port
    finally:
        semaphore.release()

async def main():
    ip = '127.0.0.1'
    portrange = (1, 65535)

    loop = asyncio.get_running_loop()

    coroutines = []

    def callback(coroutine):
        coroutines.remove(coroutine)
        result = coroutine.result()
        if result is not None:
            print(result)

    for port in range(*portrange):
        coroutines.append(loop.create_task(try_connect(ip, port)))
        coroutines[-1].add_done_callback(callback)

    i = 1
    while len(coroutines) > 0:
        print(f'doing things i want - {i}')
        i+=1
        await asyncio.sleep(1)

asyncio.run(main())
