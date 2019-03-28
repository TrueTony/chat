# asyncio, tcp server

import asyncio


list_of_users = []

async def handle_echo(reader, writer):

    name = await reader.read(1024)
    name.decode()

    addr = writer.get_extra_info('peername')
    addr2 = writer.get_extra_info('socket')
    addr3 = writer.get_extra_info('socketname')
    addr4 = writer.get_extra_info('compression')
    addr5 = writer.get_extra_info('cipher')
    addr6 = writer.get_extra_info('peercert')
    addr7 = writer.get_extra_info('sslcontext')
    addr8 = writer.get_extra_info('ssl_object')
    addr9 = writer.get_extra_info('pipe')
    addr0 = writer.get_extra_info('subprocess')

    print('peername', addr)
    print('socket', addr2)
    print('socketname', addr3)
    print('compression', addr4)
    print('cipher', addr5)
    print('peercert', addr6)
    print('sslcontext', addr7)
    print('ssl_object', addr8)
    print('pipe', addr9)
    print('subprocess', addr0)

    print(f"{addr!r} is connected !!!!")

    while True:
        data = await reader.read(1024)
        message = data.decode()
        if not message:
            del list_of_users[name]
            break
        


def msg(message):
    for user in list_of_users:
        user.write(message.encode())


async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')
    async with server:
        await server.serve_forever()

asyncio.run(main())