# More on Decoractors!

# If the decorated function has a parameter(s),
# ... the wrap_func() requires a parameter(s).
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('*********')
        func(*args, **kwargs)
        print('*********')
    return wrap_func


@my_decorator
def hello(greeting, emoji=':('):
    """
    greeting is a string
    """
    print(greeting, emoji)

@my_decorator
def bye():
    print('see ya latter')

hello('hollllaaaaaaa')#, ':)')