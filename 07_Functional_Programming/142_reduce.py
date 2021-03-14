# reduce()
# Not part of the basic python package
# map() and filter() use reduce under-the-hood
# functools --> functional programing tools
from functools import reduce
my_list = [1, 2, 3]
your_list = [10, 20, 30]
their_list = (5, 4, 3)

def only_odd(item):
    return item % 2 != 0

def mutiply_by2(item):
    return item * 2



# reduce(function, sequence)
# sequence is analagous to data.

def accumulator(acc, item):
    print(acc,item)
    return  acc + item

# 0 is the initial value within in reduce
# 0 us the initial value of "acc" in the "accumulator" fcn.
# reduce does not require the list() fcn.
print(reduce(accumulator, my_list, 0))