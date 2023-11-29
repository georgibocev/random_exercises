# 14.Nested Functions for String Manipulation
# Write a function containing nested functions to perform various string manipulations like uppercase, lowercase, and
# capitalization.
# Input: "hello", "uppercase"
# Output: "HELLO"

def string_manipulation(content, operation):
    def uppercase(s):
        return s.upper()
    def lowercase(s):
        return s.lower()
    def capitalize(s):
        return s.capitalize()
    if operation == "uppercase":
        result = uppercase(content)
    elif operation == "capitalize":
        result = capitalize(content)
    elif operation == "lowercase":
        result = lowercase(content)
    else:
        result = "Operation is not valid"
    return result


input_string = "hello"
input_operation = "uppercase"
output = string_manipulation(input_string, input_operation)
print(output)