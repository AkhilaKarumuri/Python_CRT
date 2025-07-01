class Vehicle:
    def __init__(self):
        print("I am the vehicle class constructor")
    @classmethod
    def start():
        print("Vehicle is started")
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        print("I am the Car Class constructor")
    @staticmethod
    def Start():
        print("Car is started")
C1=Car()
C1.Start()