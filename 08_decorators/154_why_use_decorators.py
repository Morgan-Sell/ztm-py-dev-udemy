# Why do we use decorators?
# Perfomance decorator to use during code testing.
# How much time is required for a funciton to execute?
# time() returns the time in milliseconds
# Decorators are commonly used in frameworks.
# Example of web frameworks are Flask and Django
# An authtentication decorator can be extremely useful.
### The function is only executed if the user is authenticated.


from time import time

def performance(fn):
    """
    Calculate the time difference betwee function start and finish.
    """
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"Took {t2-t1} ms")
        return result
    return wrapper

@performance
def long_time():
    for idx in range(1000000):
        idx * 5

long_time()