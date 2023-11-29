# 1. Задача: Създайте клас BankAccount, който да инкапсулира баланса и позволява депозиране и теглене след проверка на PIN код.
#
# Вход: PIN 1234, депозит 100, теглене 50
# Изход: баланс 50

class BankAccount:
    def __init__(self, pin):
        self.__pin = pin
        self.__balance = 0

    def is_pin_correct(self, entered_pin):
        return entered_pin == self.__pin
    def deposit(self, amount, entered_pin):
        if self.is_pin_correct(entered_pin):
            self.__balance += amount
        else:
            print("Incorrect PIN. Please try again.")

    def withdraw(self, amount, entered_pin):
        if self.is_pin_correct(entered_pin):
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                print("Not enough funds.")
        else:
            print("Incorrect PIN. Please try again.")


exPIN = 1234
wrongPIN = 2023
exAccount = BankAccount(exPIN)
print("Starting balance", exAccount._BankAccount__balance) ## I know this should not be used, I was just lazy to create a getter and wanted to learn more about name mangling
exAccount.deposit(100, exPIN)
print("Balance after successful deposit:", exAccount._BankAccount__balance)
exAccount.deposit(100, wrongPIN)
exAccount.withdraw(50, exPIN)
print("Balance after successful withdrawal:", exAccount._BankAccount__balance)
exAccount.withdraw(50, wrongPIN)
exAccount.withdraw(100, exPIN)

