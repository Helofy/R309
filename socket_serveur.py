import socket

def data(conn):
    reply = ''
    data = conn.recv(1024).decode()


    print("Client : ", data)

    if data =='bye':
        print("le client c'est déconnerté ")
        conn.send(reply.encode())

    elif data == 'arret':
        print("fermeture de la session:")
        reply= 'arret'
        conn.send(reply.encode())
        conn.close()
    else:
        reply = input("serveur :")
        conn.send(reply.encode())


if __name__ == '__main__':
    a= True
    server_socket = socket.socket()
    server_socket.bind(('127.0.0.1', 8111))
    server_socket.listen(1)
    conn, address = server_socket.accept()
    while a==True:
        try:
            data(conn)
        except ConnectionAbortedError:
            print("le client c'est déconnecté")
            conn.close()
            conn, address = server_socket.accept()
        except OSError:
            print(' DFermeture de la session')
            a = False


    conn.close()