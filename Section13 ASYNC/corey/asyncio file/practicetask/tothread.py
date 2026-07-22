from asyncio import run,to_thread,sleep,create_task
import threading
import time

def download_file(filename):
    print("downloading....")
    time.sleep(4)
    print("Download completed")
    return "success"

async def show_status():
    print("checking status")
    await sleep(2)
    print("status checked")
 
start_time=time.perf_counter()
   
async def main():
    coroutine_obj=to_thread(download_file,"File.pdf")
    task1=create_task(coroutine_obj)
    task2=create_task(show_status())
    # task1=coroutine_obj
    # task2=show_status()
    result1=await task1
    result2=await task2
    
    print(result1)
    print(result2)

run(main())
print(time.perf_counter()-start_time)
    