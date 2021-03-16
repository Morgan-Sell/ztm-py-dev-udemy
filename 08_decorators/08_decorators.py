# DECORATORS
# Functions are "first-class citizens". 
# In Python, functions can be passed around like variables
# Decorators are only possible b/c functions can act like variables.
# Decorators add extra functionality to a function.

def hello():
    print("hollaaaaaaa!")

greet = hello

# Deleting hello() will not effect greet().
del hello

# greet() is still pointing to the function.
print(greet())


####

def hello(func):
    func()

def greet():
    print('still here!')

a = hello(greet)

print(a)

# Higher Order Function (HOC) is one of two things:
# 1) a function that accepts another function
# 2) a function that returns another function

def greet(func):
    func()

def greet2():
    def func():
        return 5
    return func