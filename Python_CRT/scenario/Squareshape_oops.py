'''WAPP to create a Squareshape class & declare the properties as
Length, Breadth, Height
i) Calculate the area of square using Instance methods 
ii) Check whether the sides of Square's are equal or not using Instance methods 
iii) calculate the perimeter of square using Instance methods 
iv) Find the diagonals of square using Instance methods 
v) Find the side length of suare using Instance methods '''
class Squareshape:
    def __init__(self, length, breadth, height):
        self.length = length
        self.breadth = breadth
        self.height = height

    def area(self):
        return self.length * self.breadth

    def is_square(self):
        return self.length == self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def diagonal(self):
        return (self.length**2 + self.breadth**2) ** 0.5

    def side_length(self):
        return self.length if self.is_square() else None

    def __str__(self):
        return f"Squareshape(length={self.length}, breadth={self.breadth}, height={self.height})"
    