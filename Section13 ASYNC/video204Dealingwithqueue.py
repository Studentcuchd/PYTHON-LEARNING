# make a printer manager using queue
from threading import Thread
from queue import Queue
import random
import time

print_queue=Queue()


def add_task(message):
    time.sleep(random.random())
    print_queue.put(message)
    
    
def printer_manager():
    while True:
        time.sleep(random.random())
        task_val=print_queue.get()
        time.sleep(random.random())
        print(f"Your message = {task_val}")
        print_queue.task_done()


# creating thread for printer_manager

t1=Thread(target=printer_manager,daemon=True)
t1.start()


"""

#creating thread for add_task

but we can not use join here 

for i in range(5):
    task_input=input("Enter your task = ")
    t2=Thread(target=add_task,args=(task_input,))
    t2.start()
    
    
"""
# so we will make a list

thread_list=[]

for i in range(5):
    task_input=input("Enter your task = ")
    t2=Thread(target=add_task,args=(task_input,),daemon=True)
    thread_list.append(t2)
    # t2.start()



# ye pehle 5 input lega fir start hoga esliye loop me hi start lga do agar sath sath print chiye
for i in thread_list:
    i.start()
    
for i in thread_list:
    i.join()


print_queue.join()


