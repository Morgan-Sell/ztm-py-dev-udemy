# map()
# map is graet to use when I need to iterate through an object.

def multiply_by2(lst):
    new_list = []
    for item in lst:
        new_list.append(item*2)
    return new_list

my_list = [1, 2, 3]
def map_mutiply_by2(item):
    return item * 2

# returns a map object
#print(map(multiply_by2, [1, 2, 3]))

# Returns "TypeError: 'int' object is not iterable"
# map revmoes the need to create "new_list" and append items to "new_list"
# All that is required is action.
#print(list(map(multiply_by2, [1, 2, 3])))

print(list(map(map_mutiply_by2, my_list)))
# Note that "my_list" does not change after the map() function is applied.
# map() has NO side effects.
print(my_list)