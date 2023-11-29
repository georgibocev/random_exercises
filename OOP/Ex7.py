# 7. Задача: Създайте класове Bird, Swimmer, и Penguin, където Penguin наследява и двата класа и комбинира техните свойства.
#
# Вход: създаване на пингвин и извикване на методите за плуване и летене
# Изход: "Swimming" и "Can't fly"

class Bird:
    def fly(self):
        print("Flying")
class Swimmer:
    def swim(self):
        print("Swimming")

class Penguin(Swimmer, Bird):
    def fly(self):
        print("Can't fly")

penguin = Penguin()
penguin.swim()
penguin.fly()

