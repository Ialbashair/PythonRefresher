from functools import lru_cache
import time
import csv

timings = {}
def timer(func):
    def wrapper(n):
        s = time.perf_counter()
        r = func(n)
        e = time.perf_counter()

        timings[n] = e - s

        print(f"Finished in {e - s:.9f}s: fib({n}) - > {r}")
        return r
    return wrapper

@lru_cache(maxsize=None)
@timer
def fib(n: int) -> int:
    if n <=1:
        return n
    return fib(n-1) + fib(n - 2)

if __name__ == "__main__":  
    fib(100)
    with open('data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['n', 'time'])
       
        for n in sorted(timings.keys()):
            writer.writerow([n, timings[n]])
    