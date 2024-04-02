# დავალება 30

# შემსრულებელი: გიორგი ცუცქირიძე

## სავარჯიშო 1

# 1. შექმენი ასინქრონული event loop რომელიც ერთი წამის დაყოვნებით
# ამობეჭდავს რიცხვებს 1_დან 10_ის ჩათვლით.

# საჭირო ბიბლიოთეკების შემოტანა

import asyncio

async def event_loop():
    for i in range(1, 11):
        print(i)
        await asyncio.sleep(1)      

asyncio.run(event_loop())


## სავარჯიშო 2

# 2. დაწერე ასინქრონული ფუნქციის კოდი, რომელიც მოიცდის ორი წამი
# და შემდეგ დაბეჭდავს "Hello World!!!" 
# შექმენი event loop რომელიც ზემოხსენებულ ფუნქციას გაუშვებს.

# საჭირო ბიბლიოთეკების შემოტანა

import asyncio

async def wait_2_sec():
    await asyncio.sleep(2)
    print("Hello World!!!")

async def event_loop2():
    await wait_2_sec()

asyncio.run(event_loop2())


#------------------------------------------------------------------#