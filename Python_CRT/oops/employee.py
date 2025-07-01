class employee():
    def __init__(self, empname, empid,designation,salary,deptname):
        self.empname=empname
        self.empid=empid
        self.Designation=designation
        self.salary=salary
        self.deptname=deptname
E1=employee("Scott","EMP101","Datanalyst","25000","DeploymentTeam")
print(f"Employee Name:{E1.empname}")
print(f"Employee ID:{E1.empid}")
print(f"Employee Designation:{E1.Designation}")
print(f"Employee salary:{E1.salary}")
print(f"Employee deptname:{E1.deptname}")