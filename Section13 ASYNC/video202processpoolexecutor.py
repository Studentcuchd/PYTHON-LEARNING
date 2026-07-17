from concurrent.futures import ProcessPoolExecutor
import time

def calc():
    ans=[x**3 for x in range(10000000)]
    return ans

def more_complex(a):

    ans=[i**5 for i in range(a)]
    return sum(ans)


if __name__=="__main__":
    start_time=time.time()
    a=int(input("enter input="))  
    with ProcessPoolExecutor(max_workers=2) as executor:

        p1=executor.submit(calc)
        p2=executor.submit(more_complex,a)
        
        print(p1.result())
        print(p2.result())
    end_time=time.time()
    print(f"Time diff= {end_time-start_time}")
    