# 3.Nested Function for Calculating Factorial
# Write a function that contains a nested function to calculate the factorial of a number.
# Input: 5
# Output: 120

def calc_factorial(a):
        def inner_calc_factorial(a):
            if a == 0 or a == 1:
                return 1
            else:
                return a * inner_calc_factorial(a - 1)
        return inner_calc_factorial(a)
number = 5
result = calc_factorial(number)
print (result)