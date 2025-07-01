"""write a python program to create a product class declare the states of the class as productname, productId, price, gst, Manifacture_date, expired date
initialize using parameterized constructer
access the elements of individual objects using instance method
and delcare mutater methods as setproduct name, set product price.............. and change the values of their properties using mutator methods and print it"""
class Product:
    def __init__(self,pname,pID,price,GST,Man_date,exp_date):
        self.pname=pname
        self.pID=pID
        self.price=price
        self.GST=GST
        self.Man_date=Man_date
        self.exp_date=exp_date
    def Get_Details(self):
        print(f"product name : {self.pname}")
        print(f"product ID : {self.pID}")
        print(f"product price : {self.price}")
        print(f"product GST : {self.GST}")
        print(f"product Manufacturing Date : {self.Man_date}")
        print(f"product name : {self.exp_date}")