from threading import Thread
import random
import time
"""
This will run perfectly  as it is like a synchronous code


count=0
def increment_counter():
    global count
    count=count+1
    return count

for i in range(100):
    t1=Thread(target=increment_counter)
    t1.start()
    print(f"count= {count}")
    
 
"""

count=0
def increment_counter():
    time.sleep(random.random())
    global count
    time.sleep(random.random())
    count=count+1
    time.sleep(random.random())

    return count

for i in range(10):
    
    t1=Thread(target=increment_counter)
    time.sleep(random.random())
    t1.start()
    time.sleep(random.random())

    print(f"count= {count}")




