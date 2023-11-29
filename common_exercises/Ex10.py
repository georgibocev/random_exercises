# 10.Lambda Function to Filter Even Numbers
# Write a lambda function that filters even numbers from a given list.
# Input: [1, 2, 3, 4, 5]
# Output: [2, 4]

inputList = [1, 2, 3, 4, 5]
outputList = list(filter(lambda x: (x % 2 == 0), inputList))
print(outputList)