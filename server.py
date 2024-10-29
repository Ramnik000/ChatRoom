import threading
import socket

host= '127.0.0.1' #localHost
port= 12345 #Port to listen on

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
server.listen()