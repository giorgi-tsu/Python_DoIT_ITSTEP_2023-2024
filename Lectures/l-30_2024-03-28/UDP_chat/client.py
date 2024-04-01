import socket
import threading
import random



host = "127.0.0.1"
port = 55555    

client_port = random.randint(8000, 9000)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.bind((host, client_port))

nickname = input("Nickname: ")

def receieve():
    