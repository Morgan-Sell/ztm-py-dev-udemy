# Define a decorator


# I can increase functionaltiy by stating "@my_decorator" above function.
# The functionality is stated w/in my_decorator().
def my_decorator(func):
    def wrap_func():
        print('*********')
        func()
        print('*********')
    return wrap_func


@my_decorator
def hello():
    print('helllooooo')

@my_decorator
def bye():
    print('see ya latter')

#bye()

# decorator translation
hello2 = my_decorator(hello)
hello2()