# Python Threading Tutorial: Run Code Concurrently Using the 
# threading Module

# Learning Objectives:

# - Learning how to run code concurrently using the threading module

# 1. Why would we want to use threading? 

# We want to use threading when it's going to significantly speed up 
# our program. This speed-up comes from running different tasks 
# concurrently. Speed-ups aren't really guaranteed, so it really 
# just depends on what you are doing. 



#####################################################################
#####################################################################


# Part 1: Understanding threading using some simple sleep methods
#  (timestamp: 00-01-40)

# import time

# start = time.perf_counter()

# def  do_something():
#     print("Sleeping 1 second...")
#     time.sleep(1)
#     print("Done sleeping...")


# do_something()
# do_something()

# finish = time.perf_counter()

# print(f"finished in {round(finish-start, 2)} seconds(s)") 

# In the above case, our script is running synchronously 
# (i.e. it is running everything in order) 
# This is usually a good sign of when we can get some benefits from
# using threading and concurrency.

# CPU bound tasks are things that are crunching a lot of numbers
# and using the CPU.

# i/o bound tasks are things that are just waiting for input 
# and output operations to be completed and not really using
# the CPU that much.

# Some other examples of i/o tasks include: 

# Reading/Writing from file system
# Other file system operations
# Network operations
# Downloading stuff online

# When our tasks are i/o bound (i.e. we are doing a lot of waiting  
# around for input and output operations like reading data from disk 
# or network operations), we are going to see a lot of 
# benefits from threading.

# If our tasks are doing a lot of data crunching and are CPU bound
# then we are not going to see that much benefit from threading.
# In fact, some programs actually run slower using threads because 
# of the added overhead costs when they are creating and destroying 
# different threads. 

# If a task is CPU bound then we'll likely want to use 
# multiproccessing and run it in parallel instead.

# Now let's see how to use threading with the code above


# import threading
# import time

# start = time.perf_counter()

# def  do_something():
#     print("Sleeping 1 second...")
#     time.sleep(1)
#     print("Done sleeping...")


# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# finish = time.perf_counter()

# print(f"finished in {round(finish-start, 2)} seconds(s)") 


# Now let's create 10 threads (timestamp: 00-09-55)

# import threading
# import time

# start = time.perf_counter()

# def  do_something():
#     print("Sleeping 1 second...")
#     time.sleep(1)
#     print("Done sleeping...")

# threads = [] 

# for _ in range(10):
#     t = threading.Thread(target=do_something)
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()


# finish = time.perf_counter()

# print(f"finished in {round(finish-start, 2)} seconds(s)") 

print("\n",
      "Part x: Passing arguments into functions",
      "(timestamp: 00-12-45)",
      "\n")

# import threading
# import time

# start = time.perf_counter()

# def  do_something(seconds):
#     print(f"Sleeping {seconds} second(s)...")
#     time.sleep(seconds)
#     print("Done sleeping...")

# threads = [] 

# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()


# finish = time.perf_counter()

# print(f"finished in {round(finish-start, 2)} seconds(s)") 

print("\n",
      "Part x: Learning thread pool executor",
      "(timestamp: 00-14-30)",
      "\n")

# What we saw above, until now is the older way of doing threads.
# In this case we created threads manually. 

# Now we will do threading using the thread pool executor that has 
# been added to Python 3.2

# In a lot of cases this is an easier and more efficient way of 
# threading. 

# It also allows us to easily switch over to using multiple 
# proccesses instead of threads depending on the problem that we are
# trying to solve.

# Let's now using the thread pool executor

import concurrent.futures
import time


start = time.perf_counter()

def  do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    return "Done sleeping..."


# It's best to use the thread pool executor with a context manager

with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_something, 1) # submit method schedules
    # a function to be executed and returns a futures object. The
    # futures object encapsulates the execution of our function and 
    # allows us to check in on it after it's been scheduled. 
    # So, we can check that it's running or if it's done and also
    # check the result. So, if we grab the result then it will give
    # us the return value of the function.
    print(f1.result())

finish = time.perf_counter()

print(f"finished in {round(finish-start, 2)} seconds(s)") 