# Task: Create a class Animal with basic properties like name and sound. Extend it with subclasses for specific animals like Dog, Cat, and implement their specific behaviors.
# Example Input: dog = Dog(); dog.sound()
# Example Output: “Woof!”

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Python does not support pure virtual :("

class Dog(Animal):
    def sound(self):
        return "Woof"

class Cat(Animal):
    def sound(self):
        return "Meow"

dog = Dog("Doggo")
cat = Cat("Whiskers")

print(dog.sound())
print(cat.sound())