import time
from concurrent.futures import ThreadPoolExecutor

def task(name, delay):
    print(f"{name}-Start")
    time.sleep(delay)
    print(f"{name}-End")
    return f"{name}-Result"

names = ["A", "B", "C"]
delays = [5, 1, 4]

with ThreadPoolExecutor(max_workers=2) as executor:
    results = executor.map(task, names, delays)

    print("Inside")

    for result in results:
        print(result)

print("Outside")

