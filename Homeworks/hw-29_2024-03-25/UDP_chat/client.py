import socket
import threading
import random


# ვქმნით IP-ს და სერვერის პროტს
host = "127.0.0.1"
server_port = 55555    

# ვქმნით კლიენტის პროტს
client_port = random.randint(8000, 9000)

# ვქმნით კლიენტს

# AF_INET ნიშნავს, რომ ვიყენებთ IPv4 ოჯახს. 
# SOCK_DGRAM ნიშნავს, რომ ეს არის UDP პროტოკოლი

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# ვაბავთ კლიენტს
client.bind((host, client_port))

# კლიენტს შემოჰყავს ნიკი
nickname = input("Nickname: ")


# ვქმნით ფუნქციას შეტყობინებების მისაღებად
def receieve():
    while True:
        try:
            message, _ = client.recvfrom(1024) 
            print(message.decode())
        except:
            pass
        
# ვქმნით ძაფს სადაც ეშვება მიღების ფუქნქცია
t1 = threading.Thread(target=receieve)

# ვუშვებთ ძაფს
t1.start()

# კლიენტი აგზავნის შემოსვლის შესახებ შეტყობინებას
client.sendto(f"SIGNUP_TAG:{nickname}".encode(), (host, server_port))


# კლიენტ შეყავს მესიჯი და აგზავნის მას
# თუ დაწერს quit გამოვა ჩათიდან

while True:
    message = input("")
    if message.lower() == "quit":
        exit()
    else:
        client.sendto(f"{nickname}: {message}".encode(), (host, server_port))