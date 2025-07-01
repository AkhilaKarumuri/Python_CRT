"""WAPP to create a rectangle class and initialize the variables length & breadth using constructor and access the values using mutator methods """
class Rectangle:
    def __init__(self, length, breadth):
        self.length=length
        self.breadth=breadth
    def set_details(self):
        print(f"length:{self.length}")
        print(f"breadth:{self.breadth}")
R1=Rectangle("18","20")
R1.set_details()