# asyncio, tcp client

import asyncio


async def tcp_echo_client(message, loop):
    reader, writer = await asyncio.open_connection('localhost', 10001,
        loop=loop)

    print(f'{reader} send: {message}')
    writer.write(message.encode())
    writer.close()


loop = asyncio.get_event_loop()
message = 'hello world!'
loop.run_until_complete(tcp_echo_client(message, loop))
loop.close()