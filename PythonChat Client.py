import socket

def client_starter():
    port = input('Enter port number: ')
    name = input('Enter name: ')
    host = '127.0.0.1'

    client_main(host, port, name)

def client_main(host, port, name):
    host = str(host)
    port = int(port)
    name = str(name)

    client_socket = socket.socket()
    client_socket.connect((host, port))

    try:
        client_socket.send(name.encode('UTF-8'))

        while True:
            message = input(' => ')
            client_socket.send(message.encode('UTF-8'))

    except KeyboardInterrupt:
        client_socket.close()

client_starter()