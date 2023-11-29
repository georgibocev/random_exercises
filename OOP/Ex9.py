# Задача: Създайте система от класове за музикални инструменти, като
# някои инструменти наследяват свойства от няколко базови класа (например,
# ElectricGuitar наследява Guitar и ElectricInstrument).
# Вход: свирене на електрическа китара
# Изход: "Playing electric guitar

from abc import ABC, abstractmethod

class Instrument(ABC):
    @abstractmethod
    def playing(self):
        pass

class Guitar(Instrument):
    def playing(self):
        return "Playing the guitar"


class ElectricInstrument(Instrument):
    def playing(self):
        return "Playing eletric instrument"


class ElectricGuitar(Guitar, ElectricInstrument):
    def playing(self):
        return "Playing electric guitar"



e_guitar = ElectricGuitar()
print(e_guitar.playing())
