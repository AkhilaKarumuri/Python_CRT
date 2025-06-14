list =[10,200,840,50,150]
print(list)
print("Accessing the elements in the list using +ve indexing:")
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
print("Accessing the elements in the list using -ve indexing:")
print(list[-5])
print(list[-4])
print(list[-3])
print(list[-2])
print(list[-1])
print("Accessing the elements in the list without index:")
for i in list:
    print(i)
print("Accessing the elements in the list with index:")
for i in range(len(list)):
    print(list[i])
print("Accessing the elements in the list using while loop:")
while(i<len(list)):
    print(list[i])
    i+=1
print("Sorting the list without using sort function:")
temp=list
for i in range(0,len(temp)):
    for j in range(i+1,len(temp)):
        if temp[i]>temp[j]:
            temp[i],temp[j]=temp[j],temp[i]
print(temp)

#Concatenation of two lists
a=[1,2,3,4,5]
b=[6,7,8,9,10]
list =a+b
print(list)

#Repetation of list
# * Operator is used to repeat the elements of the list

a=[1,2,3,4,5]
r=a*3
print(r)
# In the same way we also do repetation of tuple