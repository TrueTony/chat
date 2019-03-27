# asyncio, tcp server

import asyncio


list_of_users = []

async def handle_echo(reader, writer):
    # print(f'{writer}')
    # print(f'{reader}')
    name = await reader.read(1024)
    name.decode()
    name = {name: reader}
    while name in list_of_users:

    list_of_users.append(name)
    # print(f'{name} join in the chat')
    msg(f'{name} join in the chat')
    while True:
        data = await reader.read(1024)
        message = data.decode()
        if not message:
            del list_of_users[name]
            break
        # addr = writer.get_extra_info('peername')
        # print(f'recieved {message} from {name}')


def msg(message):
    for user in list_of_users:
        user.write(message.encode())

loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, 'localhost', 10001, 
    loop=loop)
server = loop.run_until_complete(coro)
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()