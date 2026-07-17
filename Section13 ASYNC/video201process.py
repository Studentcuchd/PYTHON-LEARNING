from threading import Thread
import time
from multiprocessing import Process

def ask_user1(name):
    before_start=time.time()
    print(f"Hi bro greeting {name}")
    after_start=time.time()
    print(f"asking user input time->{after_start-before_start}")
    
def complexcalc1():
    before_start=time.time()
    [x**4 for x in range(200000)]
    after_start=time.time()
    print(f"complexcalculation time->{after_start-before_start}")
    
    
    
start_timing=time.time()

""" 
process1=Process(target=ask_user1)
process2=Process(target=complexcalc1)


2 process h vo bhi alg alg fun pe to error de skta h 

⚠️ Problem tab aa sakti hai jab ask_user1() user se input() leta ho. Multiple processes ek hi terminal se input lene ki try karein, to input/output confusing ho sakta hai.

Rule: Process(target=...) me har process ka target same bhi ho sakta hai aur different bhi.


Simple reason

Windows naya process banate waqt tumhari Python file ko dobara load/import karta hai.

process1=Process(target=ask_user1)
process2=Process(target=complexcalc1)


Agar ye directly outside hai:

process1.start()

to flow kuch aisa ban sakta hai:

Main file → Process create → file dobara load → Process create → file dobara load → ...
"""


#it is acting like a guard
if __name__=="__main__":
    name=input("enter your name=")
    process1=Process(target=ask_user1,args=(name,))
    process2=Process(target=complexcalc1)


    process1.start()
    process2.start()


    process1.join()
    process2.join()
    end_time=time.time()

    print("Timing=",end_time-start_timing)