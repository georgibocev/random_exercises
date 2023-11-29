# Write a lambda function that checks whether a given string is a palindrome
# Input = "madam"
# Output: True

is_palindrome = lambda x: x == x[::-1]
input_string = "madam"
print(is_palindrome(input))