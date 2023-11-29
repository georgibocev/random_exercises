# 12.Generator for Multiplication Table
# Write a generator function that yields the multiplication table for a given number up to n.
# Input: 3, 5
# Output: 3, 6, 9, 12, 15

def gen_multiplication_table(number, times):
    for i in range(1, times+ 1):
        yield number * i



testNumber = 3
testTimes = 5
testOutput = list(gen_multiplication_table(testNumber, testTimes))
print(testOutput)