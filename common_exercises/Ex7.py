# Write a function containing nested functions for addition, subtraction, multiplication and division. The outer function
# should take two numbers and an operator as input and return the result
# Input: 10, 5, "add"
# Output: 15

def calculator(num1, num2, operation):
    def add(num1, num2):
        return num1 + num2

    def subtract(num1, num2):
        return num1 - num2

    def multiply(num1, num2):
        return num1*num2

    def divide(num1, num2):
        if num2 != 0:
            return num1/num2
        else:
            return "Not able to divide by zero"

    if operation == "add":
        result = add(num1,num2)

    elif operation == "subtract":
        result = subtract(num1,num2)

    elif operation == "multiply":
        result = multiply(num1,num2)

    elif operation == "divide":
        result = divide(num1, num2)

    else:
        result = "Operation is not valid"
    return result


input_num1 = 10
input_num2 = 5
input_operation = "add"

output = calculator(input_num1, input_num2, input_operation)
print(output)