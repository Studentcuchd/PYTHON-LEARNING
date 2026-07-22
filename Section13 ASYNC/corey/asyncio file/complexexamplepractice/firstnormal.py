from asyncio import sleep,run,create_task
import time
async def fetch_data1(val):
    print(f"do soemthing with task {val}")
    await sleep(val)
    print(f"Done with task {val}")
    
    return f"Result of {val} task"

async def main1():
    task1=create_task(fetch_data1(1))    
    print("result 1 completed")
    task2=create_task(fetch_data1(2))
    result1=await task1

    result2=await task2
    print("result 2 completed") 
    
    return [result1,result2]

start_time1=time.perf_counter()   

result1=run(main1())

print(result1)

print(time.perf_counter()-start_time1)