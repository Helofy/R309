import socket
import threading
a = True

def envoie(server_socket):
    global a
    while a == True:
        message = input('message : ')
        server_socket.send(message.encode())
        if  message == 'arret':
            server_socket.close()
            a = False
            return a
        if message =='bye':
            print('deconnection du client')
            server_socket.accept()



def reception(server_socket):
    global a
    while a == True:
        recive = server_socket.recv(1024).decode()
        if recive == 'arret':
            server_socket.close()
            a = False
            return a
        if recive== 'bye':
            print('deconnection du client')
            server_socket.accept()


if __name__ == '__main__':
    a=True

    server_socket = socket.socket()
    server_socket.bind(('127.0.0.1', 8111))
    server_socket.listen(1)
    conn, address = server_socket.accept()


    t1 = threading.Thread(target=envoie,args=[server_socket])
    t2 = threading.Thread(target=reception,args=[server_socket])
    t1.start()
    t2.start()
    t1.join()
    t2.join()
