size=int(input("Enter the size of the list:"))
num=[]
for i in range(size):
    temp=int(input(f"Enter the element at {i} index:"))
    num.append(temp)
print(f"Given list:{num}")
print("Max Ele:",max(num))
print("Min Ele:",min(num))
print("Summation:",sum(num))
print("Sorted list:",sorted(num))