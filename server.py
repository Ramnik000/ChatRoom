import threading
import socket

host= '127.0.0.1' #localHost
port= 12345 #Port to listen on

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
server.listen()

clients=[]
nicknames=[] #nickname for each client

#broadcast function to send message to all the clients
def broadcast(message):
    for client in clients:
        client.send(message)

#handle client message
def handle(client):
    while True:
        try:
            message= client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname= nicknames[index]
            broadcast(f'{nickname} left that chat'.encode('ascii'))
            nicknames.remove(nickname)
            break 






    