import socket

def data(conn):
    global b
    global a
    b=True
    reply = ''
    data = conn.recv(1024).decode()

    if data =='bye':

        reply ='bye'
        conn.send(reply.encode())
        return a
    else:
        print("Client : ", data)
    if data == 'arret':

        reply= 'arret'
        conn.send(reply.encode())
        conn.close()
        a=True
        return(a)


    reply=input('Serveur :')

    conn.send(reply.encode())






if __name__ == '__main__':
    a= True
    b=True
    server_socket = socket.socket()
    server_socket.bind(('127.0.0.1', 8111))
    server_socket.listen(1)
    conn, address = server_socket.accept()
    while a==True:

            try:
                data(conn)
            except ConnectionAbortedError:
                print("le client c'est déconnecté")
                conn, address = server_socket.accept()
            except OSError:
                print('Fermeture de la session')
                a = False



    conn.close()