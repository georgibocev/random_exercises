# 13.Lambda Function to Apply Function to List
# Write a lambda function that takes another function and a list and applies the function to every element of the list.
# Input: lambda x: x*2, [1, 2, 3]
# Output: [2, 4, 6]

apply_lambda = lambda func, lst: [func(x) for x in lst]
input_lambda = lambda x: x * 2
input_list = [1, 2, 2]

output_list = apply_lambda(input_lambda, input_list)
print("Output:", output_list)