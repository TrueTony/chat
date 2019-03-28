# asyncio, tcp server

import asyncio


list_of_users = {}

async def handle_echo(reader, writer):

    name = await reader.read(1024)
    name.decode()

    addr = writer.get_extra_info('peername')
    addr = writer
    list_of_users[addr] = name

    print(f"{addr!r} is connected !!!!")

    while True:
        data = await reader.read(1024)
        message = data.decode()
        if not message:
            print('list of users before', list_of_users)
            del list_of_users[addr]
            print('list of users after', list_of_users)
            break
        # writer.write(message.encode())
        msg(message)


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