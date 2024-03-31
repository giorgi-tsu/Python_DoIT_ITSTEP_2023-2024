import requests
from bs4 import BeautifulSoup
import time
import threading



def get_page(address):
    while True:
        response = requests.get(address)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.title.string if soup.title else "No Title Found"
            print("Webpage Title:", title)
            print("Response Code:", response.status_code)
        else:
            print(f"Error: Failed to retrieve HTML content. Status code: {response.status_code}")
        
        time.sleep(10)


t1 = threading.Thread(target=get_page, args=["http://www.2nabiji.ge"])
t2 = threading.Thread(target=get_page, args=["http://www.rico.ge"])
t3 = threading.Thread(target=get_page, args=["http://www.girocredit.ge"])

t1.start()
t2.start()
t3.start()