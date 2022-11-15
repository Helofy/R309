import socket


def data():
    message = input("Client : ")
    if message == "bye":
        client_socket.close()
    else:
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        if data != "":
            if data == "bye":
                client_socket.close()
                print("Serveur : ", data)
            elif data == 'arret':
                print("fermeture de la session")
                reply = 'arret'
                client_socket.send(reply.encode())
                client_socket.close()

            else:

                print("Serveur : ", data)



if __name__ == '__main__':
    a= True
    client_socket = socket.socket()
    client_socket.connect(('127.0.0.1', 8111))
    while a == True:
        try:

            data()
        except OSError:
            print(' Déconnexion')
            a = False
    client_socket.close()

