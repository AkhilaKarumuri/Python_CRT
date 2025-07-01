#  WAPP to read the month number as input from the user and print the respective number of days present in that particular number
Month=int(input("Enter the Month Number: "))
if Month in [4,6,9,11]:
    print(f"The Entered Month {Month} has 30 Days:")
elif Month in [1,3,5,7,8,10,12]:
    print(f"The Entered Month {Month} has 31 Days:")
elif Month == 2:
    print(f"The Entered Month {Month} has 28 or 29 Days:")
else:
    print(f"The {Month} is Invalid")