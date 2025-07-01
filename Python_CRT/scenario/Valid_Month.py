# write a python programme to read the month number as input from the user and check weather it is a valid month number or not
Month=int(input("Enter the month number: "))
if (Month>=1 and Month <=12):
    print(f"The Entered Month Number {Month} is Valid")
else:
    print(f"The Entered Month Number {Month} is not Valid, Please enter a Valid Month Number..")