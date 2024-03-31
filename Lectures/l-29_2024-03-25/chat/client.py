import socket
import threading

nickname = input("Enter your nick: ")

host = "127.0.0.1"
port = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(host, port)

def receive():
    while True:
        try:
            message = client.recv(1024).decode("ascii")
            if message == "NICK":
                client.send(nickname.encode("ascii"))
            else:
                print(message)
        except:
            print("Error")
            client.close()
            break
        

def write():
    while True:
        message = f"{nickname}: {input("")}"
        client.send(message.encode("ascii"))

recieve_thread = threading.Thread(target=receive)
recieve_thread.start() 
wriite_thread = threading.Thread(target=write)
wriite_thread.start()

