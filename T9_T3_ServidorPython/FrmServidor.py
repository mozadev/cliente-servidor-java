from socket import *
from threading import *

clients = set()

def clientThread(clientSocket, clientAddress):
    while True:
        message = clientSocket.recv(1024).decode("UTF-8")
        print(clientAddress[0] + ":" + str(clientAddress[1]) + "" + message)

        for client in clients:
            if client is not clientSocket:
                client.send((clientAddress[0] + ":" + str(clientAddress[1]) + " " +message).encode("UTF-8"))



        if not message:
            clients.remove(clientSocket)
            print(clientAddress[0] + ":" +str(clientAddress[1]) + "disconnected")
            break

    clientSocket.close()


hostSocket = socket(AF_INET, SOCK_STREAM)
hostSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR,1)

hostIp = "localhost"
portNumber = 26000
hostSocket.bind((hostIp, portNumber))
hostSocket.listen()
print("Esperando la conexión....")

while True:
    clientSocket, clientAddress = hostSocket.accept()
    clients.add(clientSocket)
    print("Conexion de: ", clientAddress[0] + ":" + str(clientAddress[1]))

    thread = Thread(target=clientThread, args=(clientSocket, clientAddress, ))
    thread.start()


