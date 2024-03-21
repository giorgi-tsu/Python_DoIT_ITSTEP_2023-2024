import time
import threading

run = True

def printer():
    counter = 0
    while run:
        time.sleep(1)
        counter += 1
        print()
        print(counter)

def printer1():
    counter = 0
    while True:
        time.sleep(1)
        counter += 1
        print()
        print(counter)

first = threading.Thread(target=printer)
# second = threading.Thread(target=printer1, daemon=True)
first.start()
# second.start()

a = input("Press Enter To end Printer Function: ")
run = False



# def printer(seconds):
#     time.sleep(seconds)
#     print(f"Done {seconds}")


# first = threading.Thread(target=printer, args=(1,))
# second = threading.Thread(target=printer, daemon=True, args=(3,))


# start = time.time()
# # printer(2)
# # printer(3)
# first.start()
# second.start()

# first.join()
# second.join()

# end = time.time()
# print(end - start)