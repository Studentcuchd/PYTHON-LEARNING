from threading import Thread
import time
from multiprocessing import Process

def ask_user1():
    before_start=time.time()
    name=input("enter your name=")
    print(f"Hi bro greeting {name}")
    after_start=time.time()
    print(f"asking user input time->{after_start-before_start}")
    
def complexcalc1():
    before_start=time.time()
    [x**4 for x in range(200000)]
    after_start=time.time()
    print(f"complexcalculation time->{after_start-before_start}")
    
    
    
start_timing=time.time()
process1=Process(target=ask_user1)
process2=Process(target=complexcalc1)


# 2 process h to error dega 

process1.start()
process2.start()

end_time=time.time()

process1.join()
process2.join()

print("Timing=",end_time-start_timing)