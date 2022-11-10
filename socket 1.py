import socket
def aaa():
    message = input('.. :')
    client_socket.send(message.encode())
    if message == 'bye':
        client_socket.close()
    data = client_socket.recv(1024).decode()
    print(data)
    if data == 'bye':
        client_socket.close()


if __name__ == '__main__':
    client_socket = socket.socket()
    client_socket.connect(('127.0.0.1', 10000))
    while 1!=0:
        aaa()
    client_socket.close()
