from asyncio import run,to_thread,sleep,create_task,gather
import threading
import time

def load_user_data(username):
    print(f"Loading data {username}")
    time.sleep(3)
    print(f"Loading successfully {username}")

    return f"{username} data loaded"


async def fetch_notification():
    print("fetching notification")
    await sleep(2)
    print("Done fetching notification")
           
    return "5 notifications"


async def fetch_message():
    print("Fetching messages")
    await sleep(1)
    print("Done Fetching messages")

    return "10 messages"
s_time=time.perf_counter()



async def main():
    result=await gather(
        to_thread(load_user_data,"Parag.Bajaj"),
        fetch_notification(),fetch_message()
    )
    print(result)

run(main())

print(f"total time= {time.perf_counter()-s_time}")