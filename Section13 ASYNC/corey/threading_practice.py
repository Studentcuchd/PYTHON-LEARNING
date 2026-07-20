import time
from threading import Thread


from concurrent.futures import ThreadPoolExecutor,as_completed
start=time.perf_counter()

def sleeping():
    print("start")
    time.sleep(2)
    print("done")
    
# t1=Thread(target=sleeping)
# t2=Thread(target=sleeping)

# t1.start()
# t2.start()

# t1.join()
# t2.join()



# for _ in range(10):
#     t=Thread(target=sleeping) 
#     t.start()   

# # we can not use join in loop because ye synchornous bna dega so for this we will append each thread in a list


thread=[]
for _ in range(10):
    t=Thread(target=sleeping) 
    t.start()  
    thread.append(t) 

for i in thread:
    i.join()
    
end=time.perf_counter()

print(f"exact time= {end-start:.2f}")




# USE OF ThreadPoolExecutor

#1 submit -> when we want to execute function once at a time we use submit(funname,arg1,arg2,....)
print("\n")
print("\n")
print("-----------ThreadPOOL-----------")
print("\n")
print("\n")



start_exe=time.perf_counter()

def sleepinf_exe(second):
    print(f"start {second}")
    time.sleep(second)
    return f"end in {second}"
with ThreadPoolExecutor() as executor:
    
    # runner1=executor.submit(sleepinf_exe,2)
    # runner2=executor.submit(sleepinf_exe,2)

    # print(runner1.result())
    # print(runner2.result())
    
    
    # instead of writing this result again and again we will use list and as_completed method
    
    #usign list comprehensiona and as_completed method we will make obj + use loop
    
    secs=[5,4,3,2,1]
    list_runner=[executor.submit(sleepinf_exe,s) for s in secs]  
    #for submit again and again
    
    
    # to print result we will use as_completed method
    # Gives Future objects as their tasks complete

    for i in as_completed(list_runner):
        print(i.result())
end_exe=time.perf_counter()
print(f"executor timing= {end_exe-start_exe:.2f}")



print("\n")
print("using map fun")
print("\n")

start_exe1=time.perf_counter()

with ThreadPoolExecutor() as exe_map:
    second=[5,4,3,2,1]
    ans=exe_map.map(sleepinf_exe,second)
    
    for i in ans:
        print(i)
    
end_exe1=time.perf_counter()
print(f"executor timing= {end_exe1-start_exe1:.2f}")