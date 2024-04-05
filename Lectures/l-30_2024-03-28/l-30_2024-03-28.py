# ლექცია 30: L30_2024-03-28

# ლექცია ჩატარდა 2024 წლის 28 მარტს
# თემა: 1. UDP ჩათის აწყობა
#       2. მრავალგანშშტოებიანი და ასინქრონული ექო სერვერის
#         რეალიზაცია

#*******************************************************************#

# საჭირო ბიბლიოთეკების შემოტანა 


#*******************************************************************#

# ლექციის კოდი



# მეორე ნაწილი (L30_2024-03-28_01-13-06)


#  2. მრავალგანშშტოებიანი და ასინქრონული ექო სერვერის რეალიზაცია


# საჭირო ბიბლიოთეკების შემოტანა

# import asyncio

# #coroutine

# async def main():
#     print("Hello")
#     await second("LLLLLLL") # await უზრუნველჰყოფს იმას, რომ 
#     # სანამ არ დასრუდლება second თასქი, მანამ არ გადავა დაბლა
#     print("World")

# async def second(text):
#     print(text)
#     await asyncio.sleep(2) # იგივეს აკეთებს აქ რასაც ზემოთ


# asyncio.run(main())

# საჭირო ბიბლიოთეკების შემოტანა

# import asyncio

# #coroutine

# async def some(number):
#     print("Running: ", number)
#     await asyncio.sleep(1)
#     print("Finished: ", number)


# async def main():
#     print("Started!")
#     list_of_tasks = []
#     for i in range(1000):
#         list_of_tasks.append(some(i))

#     await asyncio.sleep(2)
#     await asyncio.gather(*list_of_tasks)


# asyncio.run(main())


# საჭირო ბიბლიოთეკების შემოტანა

# import asyncio

# #coroutine

# async def main():
#     print("Hello")
#     await second("...") # await უზრუნველჰყოფს იმას, რომ 
#     # სანამ არ დასრუდლება second თასქი, მანამ არ გადავა დაბლა
#     print("World")

# async def second(text):
#     print(text)
#     await asyncio.sleep(2) # იგივეს აკეთებს აქ რასაც ზემოთ


# asyncio.run(main())


# საჭირო ბიბლიოთეკების შემოტანა

# import asyncio

# #coroutine

# async def main():
#     print("Hello")
#     task = asyncio.create_task(second("..."))
#     print("World")

# async def second(text):
#     print(text)
#     await asyncio.sleep(2)


# asyncio.run(main())



# საჭირო ბიბლიოთეკების შემოტანა

import asyncio

#coroutine

async def some1():
    print("Start 1")
    await asyncio.sleep(2)
    print("Done 1")
    return {"Some1": 1}

async def some2():
    for i in range(15):
        print(i)
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(some1())
    task2 = asyncio.create_task(some2())
    value = await task1
    print(value)
    await task2


asyncio.run(main())

# timestamp: L30_2024-03-28_01-47-10