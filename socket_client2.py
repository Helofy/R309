import socket
import threading


def envoie ():
    message=input('message : ')
    client_socket.send(message.encode())
    if message == 'bye' or message =='arret':
        client_socket.close()
        a=False
        return a



def reception():
    reception=client_socket.recv(1024).decode()
    if reception =='bye' or reception =='arret':
        client_socket.close()
        a = False
        return a



if __name__ == '__main__':
    a=True
    msgclient=''
    msgserveur = ''

    client_socket = socket.socket()
    client_socket.connect(('127.0.0.1', 8111))



    while a==True:

            t1 =threading.Thread(target=envoie)
            t2=threading.Thread(target=reception)
            t1.start()
            t2.start()
            t1.join()
            t2.join()






