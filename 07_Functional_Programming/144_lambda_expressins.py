# lambda expression
# lambda is CS term
# lambda expressions are one-time anonymous fcns that only require one use.
# Anonymous fcn means that I don't define the fcn.
# Other languages have anonymous functions that are called
# Lambdas can be difficult for other programmers to understand.
"""
Syntax:
------
lambda param: action(param)
"""

from functools import reduce
my_list = [1, 2, 3]

def mutiply_by2(item):
    return item * 2

def only_odd(item):
    return item % 2 != 0

def accumulator(acc, item):
    print(acc,item)
    return  acc + item

print("Map:")
print(list(map(lambda item: item * 2, my_list)))
print("\nFilter:")
print(list(filter(lambda item: item % 2 !=0, my_list)))
print("\nReduce:")
print(reduce(lambda acc, item: acc + item, my_list))
print("\nOriginal List:")
print(my_list)