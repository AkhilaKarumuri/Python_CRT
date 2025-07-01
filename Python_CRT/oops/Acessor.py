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
E1=Employee("Akhila","EMP01","Data Analyst",80000,"DeploymentTeam")
E2=Employee("Akira","EMP02","Software Developer",100000,"DeveloperTeam")
E1.Display_Details()
E2.Display_Details()