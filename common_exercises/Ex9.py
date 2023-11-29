# 9.Generator to Yield Powers of Two
# Write a generator function that yields the powers of two up to n.
# Input: 4
# Output: 1, 2, 4, 8

def generator_power_of_two(n):
    x = 1
    for _ in range(n):
        yield x
        x *= 2


testInput = 4
testOutput = list(generator_power_of_two(testInput))
print(testOutput)