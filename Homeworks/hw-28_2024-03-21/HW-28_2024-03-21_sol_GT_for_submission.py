# დავალება 28

# შემსრულებელი: გიორგი ცუცქირიძე

## სავარჯიშო 1

# დაწერე ფუნქცია, რომელიც არგუმენტად მიიღებს ვებგვერდის მისამართს
# და გააგზავნის GET request_ს ყოველ 10 წამში და დაბეჭდავს ვებგვერდის
# სახელს და პასუხად მიღებულ სტატუსის კოდს. გამოიყენე time 
# მოდულის sleep ფუნქცია.

# Threading_ის გამოყენებით ერთდროულად გაუშვი ზემოხსენებული 
# ფუნქცია სამი განსხვავებული ვებგვერდის შესამოწმებლად.


import requests
from bs4 import BeautifulSoup
import time
import threading



def get_page(address):
    while True:
        response = requests.get(address)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.title.string if soup.title else\
                  "No Title Found"
            print("Webpage Title:", title)
            print("Response Code:", response.status_code)
        else:
            print(f"Error: Failed to retrieve HTML content."
                  f"Status code: {response.status_code}")
        
        time.sleep(10)


t1 = threading.Thread(target=get_page,
                      args=["http://www.2nabiji.ge"])
t2 = threading.Thread(target=get_page,
                      args=["http://www.rico.ge"])
t3 = threading.Thread(target=get_page,
                      args=["http://www.girocredit.ge"])


t1.start()
t2.start()
t3.start()


#------------------------------------------------------------------#