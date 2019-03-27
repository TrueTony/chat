# asyncio, tcp client

import asyncio


async def tcp_echo_client(loop):
    reader, writer = await asyncio.open_connection('localhost', 10001,
        loop=loop)
    name = input('Enter your name: ')
    writer.write(name.encode())
    while True:
        input_message = await reader.read(1024)
        if input_message:
            print(input_message)
        message = input()
        if not message:
            break
        # print(f'{name} send: {message}')
        writer.write(message.encode())
    

loop = asyncio.get_event_loop()
loop.run_until_complete(tcp_echo_client(loop))
loop.close()