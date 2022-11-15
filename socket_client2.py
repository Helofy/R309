import socket
import threading


def envoie (client_socket):
    message=input('message : ')
    client_socket.send(message.encode())
    if message == 'bye' or message =='arret':
        client_socket.close()
        a=False
        return a



def reception(client_socket):
    reception=client_socket.recv(1024).decode()
    if reception =='bye' or reception =='arret':
        client_socket.close()
        a = False
        return a



if __name__ == '__main__':


    client_socket = socket.socket()
    client_socket.connect(('127.0.0.1', 8111))


    t1 =threading.Thread(target=envoie,args=[client_socket])
    t2=threading.Thread(target=reception,args=[client_socket])
    t1.start()
    t2.start()
    t1.join()
    t2.join()






