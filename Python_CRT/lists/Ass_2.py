'''2. Print Items from a List with Specific Length
You are given a list of strings and an integer n. Write a program that prints all the strings from the list that have a length exactly equal to n.
'''

size=int(input("Enter the size of the list :"))
list=[]
count=[]
for i in range (size):
    temp=(input("Enter the element at" f" {i}: "))
    list.append(temp)
print("The list of elements are ",list)
n = int(input("Enter the length to filter by length : "))
for item in list:
    if len(item) == n:
        count.append(item)
print("Strings with length" f" {n}:", count)