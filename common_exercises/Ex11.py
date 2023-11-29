# 11.Nested Function to Calculate Exponential
# Write a function containing a nested function that calculates the exponential of a number using a given base.
# Input: 2, 3
# Output: 8

def calculate_exponential(base, exp):
    def inner_calculate_exponential(base, exp):
        if exp == 0:
            return 1
        else:
            return base ** exp
    result = inner_calculate_exponential(base,exp)
    return result


input_base = 3
input_exp = 4
output = calculate_exponential(input_base, input_exp)
print(output)
