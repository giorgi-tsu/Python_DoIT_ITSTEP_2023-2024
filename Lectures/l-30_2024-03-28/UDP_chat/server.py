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


