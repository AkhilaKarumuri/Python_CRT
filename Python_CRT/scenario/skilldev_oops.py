"""You have attended a skill Development Training program from for 15 Days on Python Programming Language
Task:
Write a python program to give the detailed report of 15 days python training which includes
1.Day
2.Topics
3.Efficiency(Rate of efficiency & grip on topics learnt on a scale of 5)
4. Number of Assignment Questions Solved
5. Number of Hackerrank Questions Solved
6. Ratings Achieved on Hackerrank for that particular day
7. Certifications Completed(including name of certificate)
8. Duration of class
9. Rate the session on scale of 5 where
i.being worst
ii.2-being bad
iii.3-being average
iv.4-being good
v.5-being best"""
class Python:
    def __init__(self, Day, Topics, Efficiency, Num_of_Assignments, Num_of_Hackerrank, Ratings_on_Hackerrank, Certifications, classduration, Rate_the_session):
        self.Day = Day
        self.Topics=Topics
        self.Efficiency=Efficiency
        self.Num_of_Assignments=Num_of_Assignments
        self.Num_of_Hackerrank=Num_of_Assignments
        self.Ratings_on_Hackerrank=Ratings_on_Hackerrank
        self.Certifications=Certifications
        self.classduration=classduration
        self.Rate_the_session=Rate_the_session
def display_details(self):
    print(f"Day:{self.Day}")   
    print(f"Topics:{self.Topics}")
    print(f"Efficiency:{self.Efficiency}")
    print(f"Num_of_Assignments:{self.Num_of_Assignments}")
    print(f"Num_of_Hackerrank:{self.Num_of_Hackerrank}")
    print(f"Ratings_on_Hackerrank:{self.Ratings_on_Hackerrank}")
    print(f"Certification:{self.Certifications}")
    print(f"classduration:{self.classduration}")
    print(f"Rate the session:{self.Rate_the_session}")
    print("-----------------------------------------")
p1=Python(1,"Basics",4,3,5,3,"Basics of pyhton","5hrs","5 star")
p2=Python(2,"DataTypes",4,13,5,3,"Data types in pyhton","5hrs","5 star")
p3=Python(3,"loops",4,10,5,3,"Loops in python","5hrs","5 star")
p4=Python(4,"conditions",4,23,5,3,"conditions","5hrs","5 star")
p5=Python(5,"list",4,3,5,3,"list","5hrs","5 star")
p6=Python(6,"string",4,13,5,3,"string","5hrs","5 star")
p7=Python(7,"tuple",4,10,5,3,"tuple","5hrs","5 star")
p8=Python(8,"Dictionary",4,23,5,3,"Dictionary","5hrs","5 star")
p9=Python(9,"boolean",4,3,5,3,"boolean","5hrs","5 star")
p10=Python(10,"OOPS",4,13,5,3,"OOPS","5hrs","5 star")
p11=Python(11,"lambda",4,10,5,3,"lambda","5hrs","5 star")
p12=Python(12,"builtin",4,23,5,3,"conditions","5hrs","5 star")
p13=Python(13,"class,object",4,3,5,3,"class,object","5hrs","5 star")
p14=Python(14,"Scenario based Questions",4,13,5,3,"Scenario based Questions","5hrs","5 star")
p15=Python(15,"Project",4,10,5,3,"Project","5hrs","5 star")
display_details(p1)
display_details(p2)
display_details(p3)
display_details(p4)
display_details(p5)
display_details(p6)
display_details(p7)
display_details(p8)
display_details(p9)
display_details(p10)
display_details(p11)
display_details(p12)
display_details(p13)
display_details(p14)
display_details(p15)