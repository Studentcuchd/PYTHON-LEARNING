from asyncio import sleep,run,create_task
# This is a coroutine

async def async_greet_fun(name):
    print("Asynchronous function")
    
    await sleep(0.1)
    return f"Hi {name}"
    

# Creating coroutine obj and printing result
# async def main():
#     coroutine_obj= async_greet_fun("Parag")
#     print(f"Coroutine object={coroutine_obj}")
    
#     coroutine_result=await coroutine_obj
#     print(coroutine_result)

# if __name__=="__main__":   
#     run(main())
    
    
"""  
use of task and we use var_name=create_task(async fun())

"""
async def main():
    task= create_task(async_greet_fun("Parag"))
    print(f"task printing =  {task}")
    
    task_result=await task
    print(task_result)

if __name__=="__main__":   
    run(main())
    
    
