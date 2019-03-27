# asyncio, tcp client

import asyncio


async def tcp_echo_client(message, loop):
    reader, writer = await asyncio.open_connection('localhost', 10001,
        loop=loop)
    addition = message/1000
    while True:
        print(f'{reader} send: {message}')
        message = str(message)
        writer.write(message.encode())
        await asyncio.sleep(1+addition)
    
    

loop = asyncio.get_event_loop()

task_list = [loop.create_task(tcp_echo_client(i, loop)) for i in range(500)]

loop.run_until_complete(asyncio.wait(task_list))
# loop.run_until_complete(loop.create_task(tcp_echo_client(0, loop)))
# loop.run_until_complete(asyncio.gather(task_list))

#loop.run_until_complete(tcp_echo_client(loop))

loop.close()