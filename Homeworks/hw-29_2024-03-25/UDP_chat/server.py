import socket
import threading
import queue


# ვამზადებთ მონაცემთა სტრუქტურას შეტყობინებების შესანახად
messages = queue.Queue()

# ვქმნით სიას კლიენტების შესანახად
clients = []

# ვქმნით IP-ს და პროტს
host = "127.0.0.1"
port = 55555

# ვქმნით სერვერს

# AF_INET ნიშნავს, რომ ვიყენებთ IPv4 ოჯახს. 
# SOCK_DGRAM ნიშნავს, რომ ეს არის UDP პროტოკოლი

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# სერვერის გაშვება
server.bind((host, port))

# ვქმნით ფუნქციას, რომელიც მიიღებს შეტყობინებებს

def receive():
    print("Server Started!")
    while True:
        try:
            # სერვერი მიიღებს შეტყობინებას და კლიენტის მისამართს
            message, addr = server.recvfrom(1024)
            # ვინახავთ შეტყობინებას "ბაზაში"
            messages.put((message, addr))
        except:
            pass


# ვქმნით ფუნქციას, რომელიც ყველა კლიენტს გაუგზავნის ერთის მიერ 
# გამოგზავნილ შეტყობინებას
        
def broadcast():
    while True:
        # სანამ შეტყობინებების "ბაზაში" რაიმე იქნება ეს ციკლი სულ
        # იმუშავებს
        while not messages.empty():
            # შეტყობინებების ბაზიდან ვიღებთ შეტყობინებას და 
            # გამომგზავნის მისამართს
            message, addr = messages.get()
            print(message.decode())
            # თუ ახალი კლიენტი შემოუერთდა ჩათს დაემატება 
            # კლიენტების სიაში
            if addr not in clients:
                clients.append(addr)

            for client in clients:
                try:
                    # ამოვიღებთ ნიკს და გავაგზავნით შეტყობინებას 
                    # ყველა კლიენტთან
                    #SIGNUP_TAG:Elene
                    if message.decode().split(":")[0] == "SIGNUP_TAG":
                        name = message.decode()[11:]
                        server.sendto(f"{name} Joined!".encode(), client)
                    else:
                        server.sendto(message, client)
                except:
                    clients.remove(client)

# ვქმნით სერვერის ფუნქციების ძაფებს
t1 = threading.Thread(target=receive)
t2 = threading.Thread(target=broadcast)

# ვუშვებთ სერვერის ფუნქციების ძაფებს
t1.start()
t2.start()
