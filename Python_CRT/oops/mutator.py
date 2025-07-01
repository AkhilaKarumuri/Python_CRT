"""This method is used to access or read and modify data of variables.
This method modify the data in the variable
This is also called setter method
Ex:
def set_value(self):
def set_result(self):
def set_name(self):
def set_id(self):
"""
class Mobile:
    def __init__(self,P,C,B):
        self.Price=P
        self.Color=C
        self.Brand=B
        print("Object is Created")
    #Mutator
    def Set_Color(self):
        self.Color='Blue'
    #Accessor
    def Get_Details(self):
        print(f"Color : {self.Color}")
        print(f"Price : {self.Price}")
        print(f"Brand : {self.Brand}")
M1=Mobile("12000",'Black','samsung')
M1.Set_Color()
M1.Get_Details()