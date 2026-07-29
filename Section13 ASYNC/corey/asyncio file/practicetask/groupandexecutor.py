from asyncio import run,to_thread,get_running_loop,sleep,TaskGroup,taskgroups,create_task
import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor


def load_file(filename):
    print(f"loading {filename}")
    time.sleep(2)
    print(f"{filename} loaded")
    
    return filename


async def run_in_thread(loop,executor,filename):
    result=await loop.run_in_executor(
        executor,load_file,filename
    )
    return result


def calculate_score(number):
    total=0
    for i in range(10000000):
        total+=i%number
        
    return total

async def process_pool(loop,executor,number):
    result=await loop.run_in_executor(
        executor,calculate_score,number
    )
    return result


async def fetch_live_status():
    print(f"Fetching live status")
    await sleep(1)
    print("Live status received")
    
    return "System online"


satrt_time=time.perf_counter()
async def main():
    loop=get_running_loop()
    with ThreadPoolExecutor(max_workers=2) as thread_executor:
        with ProcessPoolExecutor(max_workers=2) as process_executor:
            
            async with TaskGroup() as tg:
                task1=tg.create_task(run_in_thread(
                    loop,thread_executor,"pdf.csv"
                ))
                
                task2=tg.create_task(
                    run_in_thread(
                        loop,thread_executor,"order.csv"
                    )
                )

                task3_process=tg.create_task(
                    process_pool(
                        loop,process_executor,11
                    )
                )
                
                task4_process=tg.create_task(
                    process_pool(
                        loop,process_executor,3
                    )
                )
                
                task5_normal=tg.create_task(fetch_live_status())
            
            print(task1.result())
            print(task2.result())
            print(task3_process.result())
            print(task4_process.result())



if __name__=="__main__":
    run(main())
    
print(f"time= {time.perf_counter()-satrt_time}")
