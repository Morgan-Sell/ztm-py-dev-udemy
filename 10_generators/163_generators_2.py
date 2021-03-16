# Generaors 2
# Iterable objects have the Dunde method of "__init__".


# def make_list(num):
#     result = []
#     # range() does not create a list in memory.
#     # 
#     for i in range(num):
#         result.append(i*2)
#     return result

# "yield" pauses the function
# Only holds one item in memory
# "yield" keeps track of the state, which is referred to as the "value".
def generator_func(num):
    for i in range(num):
        yield i*2

# for item in generator_func(1000):
#     print(item)

# returns a generator object
# g = generator_func(100)
# next(g)

# "next" instructs the code to return to the function when "yield" is called.
g = generator_func(100)
next(g)
next(g)
print(next(g))