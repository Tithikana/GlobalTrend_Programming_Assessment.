import time
import functools

def measure_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        exe_time=end_time - start_time
        print(f"Function {func.__name__} executed in {exe_time:.4f} seconds")
        return result
    return wrapper

@measure_time
def expensive_task(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total

result= expensive_task(10000000)
print("Result:",result)
