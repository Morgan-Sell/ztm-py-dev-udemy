# filter()
# Sometimes return less elements than inputted into the function.
# another example is to omit usernames that start w/ a selected letter

my_list = [1, 2, 3]

def only_odd(item):
    return item % 2 != 0

# filter accepts a "function signature"
print(list(filter(only_odd, my_list)))
