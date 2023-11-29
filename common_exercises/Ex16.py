# 16.Function to Compute Power of Variable Arguments
# Write a function that takes a variable number of arguments and returns the result of raising the first argument to the
# power of the rest in order.
# Input: 2, 3, 2
# Output: 64 (i.e., 2^3^2 = 64)

def power_of_arguments(base, *exponents):
    result = base
    for exponent in exponents:
        result = result ** exponent
    return result

base = 2
exponents = [2, 3]
output_number = power_of_arguments(base, *exponents)
print("Output:", output_number)