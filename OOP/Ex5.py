# 5. Задача: Реализирайте клас TemperatureConverter със статични методи за конвертиране между градуси Целзий и Фаренхайт.
#
# Вход: конвертиране на 32 градуса Целзий до Фаренхайт
# Изход: 89.6 градуса Фаренхайт

class TemperatureConverter:

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit_degrees):
        return (fahrenheit_degrees - 32) * 5/9, "°C"

    @staticmethod
    def celsius_to_fahrenheit(celsius_degrees):
        return (celsius_degrees * 9/5) + 32, "°F"

exampleResult = TemperatureConverter.celsius_to_fahrenheit(32)
print(exampleResult)