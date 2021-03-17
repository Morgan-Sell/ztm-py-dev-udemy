# Under the Hood of Generators

def special_for(iterable):
    iterator = iter(iterable)
    # iter() allows function to use the following code
    while True:
        try:
            print(iterator)
            # next() returns the following item
            print(next(iterator) * 2)
        except StopIteration:
        # no more remaining elements in the iterable.
            break

# Each element is located at the same space. See output.
#special_for([1, 2, 3])

class MyGen():
    current_iter = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current_iter < self.last:
            num = MyGen.current_iter
            MyGen.current_iter += 1
            return num
        raise StopIteration

gen = MyGen(0, 100)
for i in gen:
    print(i)