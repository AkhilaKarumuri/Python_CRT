class Employee:
    def __init__(self,Empname,EmpID,Designation,Salary,DeptName): # constructor format fixed
        print("Object is created.")
        self.Empname=Empname
        self.EmpID=EmpID
        self.Designation=Designation
        self.Salary=Salary
        self.DeptName=DeptName
def Display_Details(self):
    print(f"Employee Name : {self.Empname}")
    print(f"Employee ID : {self.EmpID}")
    print(f"Employee Designation : {self.Designation}")
    print(f"Employee Salary : {self.Salary}")
    print(f"Department Name : {self.DeptName}")
E1=Employee("Akhila","EMP01","Data Analyst",25000,"DeploymentTeam")
E2=Employee("Rahul","EMP02","tester",35000,"TestingTeam")
E3=Employee("Amul","EMP03","Data Scientist",45000,"Teamlead")
E4=Employee("Sony","EMP04","Cloudengineer",55000,"project")
E5=Employee("Nani","EMP05","product manager",15000,"product")
E6=Employee("Anu","EMP06","Management",65000,"hr")
Display_Details(E1)
Display_Details(E2)
Display_Details(E3)
Display_Details(E4)
Display_Details(E5)
Display_Details(E6)