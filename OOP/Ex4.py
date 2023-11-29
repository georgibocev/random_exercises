# 4. Задача: Създайте клас Calculator, който предоставя статични методи за основни аритметични операции.
#
# Вход: събиране на 5 и 3
# Изход: 8

class Calculator:

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y != 0:
            return x / y
        else:
            return "You are not able to divide by zero"

exampleResult = Calculator.add(5,3)
print(exampleResult)