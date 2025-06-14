size=int(input("Enter the length of the list:"))
list=[]
even=[]
odd=[]
for i in range(size):
    temp=input("Enter the element at" f" {i}th index:")
    list.append(temp)
print(list)
for i in range(0,size):
    if i%2==0:
        even.append(list[i])
    else:
        odd.append(list[i])
print(even)
print(odd)