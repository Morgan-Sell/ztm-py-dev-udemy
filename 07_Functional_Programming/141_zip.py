# zip()
# Accepts 2 or more iterables and coalesces them
# Can zip a list and tuple.
# the primary requirement is that the variables are an iterable.

my_list = [1, 2, 3]
your_list = [10, 20, 30]

print(list(zip(my_list, your_list)))