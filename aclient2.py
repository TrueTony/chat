# asyncio, tcp client

import asyncio


async def tcp_echo_client():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    name = input('Enter your name: ')
    writer.write(name.encode())
    while True:
        # input_message = await reader.read(1024)
        # if input_message:
        #    print(input_message)
        message = input()
        if not message:
            break
        # print(f'{name} send: {message}')
        writer.write(message.encode())
        input_message = await reader.read(1024)
        if input_message:
            print('print', input_message)
    

async def main():
    await tcp_echo_client()


asyncio.run(main())
