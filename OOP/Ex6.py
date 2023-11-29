# 6.Задача: Създайте клас UserData, който използва статични свойства за съхранение на общи данни за
# потребителите в система и методи за тяхното управление.
# Вход: добавяне на потребител "Bob"
# Изход: списък с потребители: ["Bob"]

class UserData:
    users = []

    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    @classmethod
    def add_user(cls, name, phone, email):
        created_user = UserData(name, phone, email)
        cls.users.append(created_user)
        return created_user

    @classmethod
    def get_users(cls):
        return cls.users[:]

example = UserData.add_user("Ivan", "431431431", "ivan@codeacademy.com")
example2 = UserData.add_user("Bob", "4319431431", "bob@codeacademy.com")

all_created_users = UserData.get_users()
for user in all_created_users:
    print(f"Name: {user.get_name()}, Phone: {user.get_phone()}, Email: {user.get_email()}")