'''Divide All Elements of a List by a Number
Write a program that accepts a list of numbers and a divisor. Divide each element of the list by the divisor and return a new list with the results. Ensure the divisor is not zero.'''
n= int(input("Enter the size of the list: "))
list=[]
for i in range(n):
    temp=int(input(f"Enter element {i}: "))
    list.append(temp)
print("The list of numbers is :",list)
divisor = int(input("Enter the divisor: "))
if divisor ==0:
    print("The division by 0 is not possible enter another number")
else:
    for i in list:
        result = i // divisor
        print(f"The result of dividing {i} by {divisor} is: {result}")