# 2. Задача: Реализирайте клас Person, който инкапсулира личните данни и предоставя методи за промяна само след валидация с парола.
#
# Вход: парола "secret", промяна на имейл
# Изход: новият имейл

class Person:
    def __init__(self, password, email, phone_number):
        self.__password = password
        self.__email = email
        self.__phone_number = phone_number

    def change_email(self, new_email, entered_password):
        if self.is_password_correct(entered_password):
            self.__email = new_email
            return new_email
        else:
            return "Incorrect password"

    def change_phone_number(self, new_phone_number, entered_password):
        if self.is_password_correct(entered_password):
            self.__phone_number = new_phone_number
            return new_phone_number
        else:
            return "Incorrect password"

    def forgotten_password(self, email, phone_number):
        if email == self.__email and phone_number == self.__phone_number:
            new_password = input ("Enter a new password")
            self.__password = new_password
            return "Password changed"
        else:
            return "Incorrect email or phone number"

    def is_password_correct(self, entered_password):
        return entered_password == self.__password


expassword = "secret"
exphone_number = "0214214214"
exemail = "gosho@abv.bg"
new_exemail = "codeacademy@aaa.bg"
chovek = Person(expassword, exemail, exphone_number)
print(chovek._Person__email)
chovek.change_email(new_exemail, expassword)
print(chovek._Person__email)