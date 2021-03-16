# Evaluate generator performance
# Generators are very useful when using long loops.
# Many Python libraries use generators undearneath the hood.

from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"took {t2-t1} millisecs")
        return result
    return wrapper

@performance
def long_time():
    """
    Removes prior integers from memory.
    """
    print('1')
    for i in range(10000000):
        i*5

@performance
def long_time2():
    print('2')
    for i in list(range(10000000)):
        i*5
    
# long_time2() is > 1.5x longer than long_time()
long_time()
long_time2()