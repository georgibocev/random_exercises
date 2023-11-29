# 8.Lambda Function to Sort a List of Tuples
# Write a lambda function that takes a list of tuples and sorts them by the second element.
# Input: [(1, 2), (3, 1), (5, 0)]
# Output: [(5, 0), (3, 1), (1, 2)]

input_test = [(1, 2), (3, 1), (5, 0)]
output_test = sorted(input_test, key=lambda x: x[1])
print("Output:", output_test)