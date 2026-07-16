import time

# single threading 


def ask_user():
    before_start=time.time()
    name=input("enter your name=")
    print(f"Hi bro greeting {name}")
    after_start=time.time()
    print(f"asking user input time->{after_start-before_start}")
    
def complexcalc():
    before_start=time.time()
    [x**4 for x in range(200000)]
    after_start=time.time()
    print(f"complexcalculation time->{after_start-before_start}")

before_call=time.time()
ask_user()
complexcalc()
after_call=time.time()

print("diff of fun before call and after call=",after_call-before_call)



print("\n")
print("\n")
print(f"-----------multithreading----------")
print("\n")
# Multithreading code
from threading import Thread

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
    
    
thread_1=Thread(target=ask_user1)
thread_2=Thread(target=complexcalc1)




before_call1=time.time()

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()




after_call1=time.time()
print("Time diff after threading=",after_call1-before_call1)