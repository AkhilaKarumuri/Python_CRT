class Person:
    def __init__(self,Name, Age, Gender):
        self.name=Name
        self.Age=Age
        self.Gender=Gender
    def PersonDetails(self):
        print(f"person's Name :{self.Name}")
        print(f"person's Age :{self.Age}")
        print(f"person's Gender :{self.Gender}")
class Patient(Person):
    def __init__(self,Name,Age,Gender,Disease):
        super(). __init__(Name, Age, Gender)
    def PatientDetails(self):
        print(f"patient's name : {self.name}")
        print(f"patient's Age : {self.Age}")
        print(f"patient's Gender : {self.Gender}")
        print(f"patient's Disease : {self.Disease}")
class Doctor(Person):
    def __init__(self,Name, Age, Gender,Specialization):
        super(). __init__(Name, Age, Gender)
        self.specialization = Specialization
        self.patient=[]
    