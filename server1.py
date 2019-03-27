import socket
import argparse


HOST = 'localhost'
PORT = 50007


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    sock.listen(socket.SOMAXCONN)
    print('Server run!')
    while True:
        conn, addr = sock.accept()
        # conn.settimeout(5)
        with conn:
            print(f'{addr} has connected!')
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(data.decode('utf8'))
                conn.sendall(data)
