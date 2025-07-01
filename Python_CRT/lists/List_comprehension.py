Num=[]
for i in range(1,11):
    Num.append(i)
print(Num)
#Implementing using list comprehension
#new_list=[expression for item un iterable_object if_statement]
New=[i for i in range(1,11)]
print(New)

"""WAPP to print even numbers from 1 to n using list comprehension"""
n=int(input("Enter the value of n: "))
Even=[i for  i in range(2,n+1) if i %2==0]
print(Even)