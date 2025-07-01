# @classmethod & @staticmethod are used as decorators in python
class Mobile:
    def __int__(self):
        print("Object is created")
    @classmethod
    def Display(Class):
        print("I am a class method")
        print("I will work irrespectibve of object creation")
Mobile.Display()
M1=Mobile()
M1.Display

#Static Method --> Static methods are used when some processing is related to the cls but does not need the class or its instances to perform any work. We use static method when we want to pass some values from outside and perform some action in the method.
class Mobile:
    def __int__(self):
        print("Object is created")
    @staticmethod
    def Display():
        print("I am a class method")
        print("I will work irrespectibve of object creation")
Mobile.Display()
M1=Mobile()
M1.Display