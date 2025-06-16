class student:
     def __init__(self):
        print("Hey..!! I am a constructor, I will be automatically invoked when the object is created")
s1=student()
s2=student()
s3=student()

class Employee:
    def __init__(self):
        print("Employee class constructor has been called..!")
E1=Employee()
E2=Employee()

"""WAPP to create a mobile class and perform instantion for 10 objects"""
class Mobile:
        def __init__(self):
             print("Mobile class constructor has been called..!")
M1=Mobile()
M2=Mobile()
M3=Mobile()
M4=Mobile()
M5=Mobile()
M6=Mobile()
M7=Mobile()
M8=Mobile()
M9=Mobile()
M10=Mobile()

""" print the address and datatype of every object"""
print(id(M1))
print(type(M1))