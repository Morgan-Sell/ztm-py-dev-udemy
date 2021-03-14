# EXERCISE - COMPREHENSION
# Using comprehensions identify that characters that occur more than once in the list.

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []

dct = {char: some_list.count(char) for char in some_list}
res = list({k:v for k,v in dct.items() if v > 1}.keys())

print(res)

# Andrei's Answer

duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)