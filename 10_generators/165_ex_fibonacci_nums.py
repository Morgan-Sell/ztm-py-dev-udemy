# Fibonacci Sequence
# Create a function to calculate the number associatted with a given index

def fib_seq_arr(num):
    seq = [0, 1]

    for n in range(2, num+1):
        tmp = seq[n-2] + seq[n-1]
        seq.append(tmp)
    return seq

print(fib_seq_arr(20))


def fib_gen(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        tmp = a
        a = b
        b = tmp + b

for x in fib_gen(20):
    print(x)