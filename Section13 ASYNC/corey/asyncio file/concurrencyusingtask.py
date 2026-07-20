from asyncio import run,sleep,create_task
import time

print("\n")
print("\n")
print("-----------------Coroutine object--------------")
print("\n")
print("\n")

async def fetch_data(val):
    print(f"do soemthing with task {val}")
    await sleep(val)
    print(f"Done with task {val}")
    
    return f"Result of {val} task"

async def main():
    obj_1=fetch_data(1)
    obj_2=fetch_data(2)
    
    result1=await obj_1
    print("result 1 completed")

    result2=await obj_2
    print("result 2 completed") 
    
    return [result1,result2]

start_time=time.perf_counter()   

result=run(main())

print(result)

print(time.perf_counter()-start_time)



# USING TASK

print("\n")
print("\n")
print("-----------------task--------------")
print("\n")
print("\n")


async def fetch_data1(val):
    print(f"do soemthing with task {val}")
    await sleep(val)
    print(f"Done with task {val}")
    
    return f"Result of {val} task"

async def main1():
    task1=create_task(fetch_data1(1))
    task2=create_task(fetch_data1(2))
    
    result1=await task1
    print("result 1 completed")

    result2=await task2
    print("result 2 completed") 
    
    return [result1,result2]

start_time1=time.perf_counter()   

result1=run(main1())

print(result1)

print(time.perf_counter()-start_time1)