import socket

def server_starter():
    port = input('Enter port number: ')
    host = '127.0.0.1'

    server_main(host, port)

def server_main(host, port):
    host = str(host)
    port = int(port)

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(3)

    client_socket, addr = server_socket.accept()

    try:
        name = client_socket.recv(1024).decode('utf-8')
        print(f'Client {name} connected')

        while True:
            message = client_socket.recv(1024).decode('utf-8')

            if not name:
                break

            print(f'{name}' + ' >> ' + f'{message}')

    except KeyboardInterrupt:
        server_socket.close()

server_starter()
