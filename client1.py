import socket
import argparse


HOST = 'localhost'
PORT = 50007

#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
with socket.create_connection((HOST, PORT)) as sock:
    print('client alive')
    # sock.connect((HOST, PORT))
    while True:
        output = input()
        # sock.sendall(b'Hello world!')
        sock.send(bytes(output, encoding='utf8'))
        data = sock.recv(1024)
        print(data)