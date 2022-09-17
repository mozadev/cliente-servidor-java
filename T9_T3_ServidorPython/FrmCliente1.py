from socket import*
from threading import*
from tkinter import *


clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

hostIp = "localhost" # hostIp = input("direccion del servidor")
portNumber = 26000 # portNumber= int( input(port:))

clientSocket.connect((hostIp, portNumber))

appcliente = Tk()
appcliente.title("Aplicacion Cliente Python")
appcliente.config(bg="#6699CC")

lblTitulo=Label(text="Cliente Python", font=("Candara", 16),bg="#6699CC")
lblTitulo.grid(row=0, column=1, padx=50, pady=10)

txtMensajes = Text(appcliente , width=50)
txtMensajes.grid(row=1, column = 1,padx= 10, pady= 10)

lblMensaje = Label(text="Mensaje:", font=("Candara",12),bg="#6699CC").place(x=10,y=460)

txtTuMensaje = Entry(appcliente, width=45)
txtTuMensaje.insert(0," ",)
txtTuMensaje.grid(row=2,column=1,padx=10,pady=10)

def enviarMensaje():
    clientMessage = txtTuMensaje.get()
    txtMensajes.insert(END, "\n" + "Cliente 1: "+clientMessage)
    clientSocket.send(clientMessage.encode("UTF-8"))
    txtTuMensaje.delete(0,"end")

btnSendMessage = Button(appcliente, text="Enviar",width=20,command=enviarMensaje)
btnSendMessage.grid(row=3, column=1,padx=10,pady=10)

def recibirMensaje():
    while True:
        serverMessage = clientSocket.recv(1024).decode("UTF-8","strict")
        print(serverMessage)
        txtMensajes.insert(END, "\n" + "Cliente 2: " + serverMessage)


recvThread = Thread(target=recibirMensaje)
recvThread.daemon = True
recvThread.start()
appcliente.mainloop()