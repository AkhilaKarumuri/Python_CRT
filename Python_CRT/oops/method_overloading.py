class Mobile:
    def __init__(self):
        print("Object is created")
def unlockmobile():
    print("Swipe up to unlock your mobile")
unlockmobile()
def unlockmobile(password):
    print("Draw a password to unlock you")
unlockmobile("123")
def unlockmobile(num,pattern):
    print("Enter your pin to unlock your mobile")
unlockmobile(4,"NNNN")

"""WAPP to create an employee class and declare the states and create 5 objects using different constructors--->Constructor overloading"""

class Employee:
    def __init__(self, Empname, EmpId, Job, Salary, Location, Dept):
        self.Empname=Empname
        self.EmpId=EmpId
        self.Job=Job
        self.Salary=Salary
        self.Location=Location
        self.Dept=Dept
        print("I am a 6 parameterized constructor")
    def __init__(self,Empname, EmpId, Job, Salary, Location):
        self.Empname=Empname
        self.EmpId=EmpId
        self.Job=Job
        self.Salary=Salary
        self.Location=Location
        print("I am a 5 parameterized constructor")
    def __init__(self,Empname, EmpId, Job, Salary):
        self.Empname=Empname
        self.EmpId=EmpId
        self.Job=Job
        self.Salary=Salary
        print("I am a 4 parameterized constructor")
    def __init__(self,Empname, EmpId, Job):
        self.Empname=Empname
        self.EmpId=EmpId
        self.Job=Job
        print("I am a 3 parameterized constructor")
    def __init__(self,Empname, EmpId):
        self.Empname=Empname
        self.EmpId=EmpId
        print("I am a 2 parameterized constructor")
    def __init__(self,Empname):
        self.Empname=Empname
        print("I am a 1 parameterized constructor")
    def __init__(self):
        print("I am a 0 parameterized constructor")
E1=Employee()
E2=Employee("Sam")
E3=Employee("Rashmitha")
E4=Employee("Akhil")
E5=Employee("Amulya")
E6=Employee("Akhila")