# • 8. Задача: Реализирайте класове за различни видове транспорт (например,
# Car, Boat) и специален клас AmphibiousVehicle, който наследява и двата.
# Вход: създаване на водолазно превозно средство и движение по суша и вода
# Изход: "Driving on land" и "Sailing on water«

class Car:
    def driving(self):
        return "Driving on land"

class Boat:
    def sailing(self):
        return "Sailing on water"

class AmphibiousVehicle(Car, Boat):
    pass

amp_vehicle = AmphibiousVehicle()
print(amp_vehicle.sailing())
print(amp_vehicle.driving())