"""If it walks like a duck and talks like a duck then it must be duck"""
class Duck:
    def walk(self):
        print("thapak thapak thapak")
class Horse:
    def walk(self):
        print("tabdak tabdak tabdak")
def myfunction(obj):
    obj.walk()
d=Duck()
myfunction(d)
h=Horse()
myfunction(h)

'''Encapsulation:- It is a process of Wrapping the states & Behaviours of an Entity into a single container for Data Security & Accessing it using Data Handlers Methods (Getter & Setter)
Abstraction:- Process of hiding the implementation and providing the functionalities to the user
Interface:- Intermediate between service and consumer'''