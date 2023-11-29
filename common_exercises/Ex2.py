# 2.Generator to Yield Fibonacci Sequence
# Write a generator function that yields the Fibonacci sequence up to n numbers.
# Input: 5
# Output: 0, 1, 1, 2, 3

def gen_fibonacci(n):
    counter = 0
    x, y = 0, 1
    while n > counter:
        yield x
        x, y = y, x+y
        counter += 1

fib_seq = list(gen_fibonacci(5))
print("Output:", ", ".join(map(str, fib_seq)))
