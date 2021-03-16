# Generators
# Generators create a sequence of values over time.
# range() is an example of a generator.
# Generators can use a special keyword "yield".
# "yield" can pause and resume functions

"""
range(100)

The code below essentially performs make_list().
list(range(100))
"""

def make_list(num):
    result = []
    # range() does not create a list in memory.
    # 
    for i in range(num):
        result.append(i*2)
    return result

# my_list points to a location in memory.
my_list = make_list(100)
print(my_list)