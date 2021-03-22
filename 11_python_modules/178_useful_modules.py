from collections import Counter, defaultdict, OrderedDict

# Counter()
# creates a dictionary that keeps track the number of occurrence of an item in an interable.
# Useful when solving optimization problems.
# Useful to count duplicate emails or similar items.
l = [1, 2, 3, 4, 5, 6, 7, 7]
sentence = "blah blah blah thinking about python"
#print(Counter(l))
#print(Counter(sentence))

# DefaultDict()
# Returns a default value if the specified key does not exist.
# Requires a "callable object" as the default value.
dictionary = defaultdict(lambda: 5, {'a': 1, 'b': 1})
# print(dictionary['c'])

# OrderedDict()
# Retains the order of how the key-value pairs were inserted.
# OrderedDict() has greater storage complexity than a "normal" dictionary.
d = {'c': 100}
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

# Starting in version 3.7, dictionaries maintain their order.