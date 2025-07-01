'''Problem:
Sort a list of dates provided in DD-MM-YYYY format chronologically.
Input:
An integer n (1<=n<=100)
A list of n strings in DD-MM-YYYY format
Output:
Sorted list of dates(earliest to latest)
---------
Example:
Input: ["12-05-2023","01-01-2022","15-08-2021"]
Output:["15-08-2021","01-01-2022","12-05-2023"]
'''
n=int(input("Enter the no.of.Dates :"))
List=[]
for i in range(n):
    print(f"Enter the {i}st Date:")
    