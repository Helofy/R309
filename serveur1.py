import socket

def aaa(conn):
    data = conn.recv(1024).decode()
    print(data)
    reply = input('...:')
    conn.send(reply.encode())
if __name__ == '__main__':
    server_socket = socket.socket()
    server_socket.bind(('127.0.0.1', 10000))
    server_socket.listen(1)
    conn, address = server_socket.accept()
    while 1!=0:
        aaa(conn)
    conn.close()
