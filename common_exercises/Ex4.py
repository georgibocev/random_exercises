# Write a function that takes a number n and returns a lambda function that multiplies its input by n
# input: 3
# output: a function that multiplies its input by 3

def multiply_by_number(n):
    return lambda x: x * n

number = 3
multiply_function = multiply_by_number(number)

test = 4
result = multiply_function(test)
print(result)