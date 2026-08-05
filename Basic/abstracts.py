#Abstraction   example using abstract method
from abc import ABC, abstractmethod
class Car(ABC):
    def show(self ):
        print("All four wheeler have four wheels")
    @abstractmethod
    def speed(self):
        pass
class Maruti(Car):
    def speed(self):
        print("Maruti has MAX Speed 180 km/hr")
class Scoda(Car):
    def speed(self):
        print('scoda has MAX speed 300 km/hr ')
m=Maruti()
s=Scoda()
m.speed()
m.show()
s.speed()
s.show()

