str="AKHILA"
for i in range(len(str)):
    for j in range(len(str)):
        print(f"{str[j]} ", end="")
    print()

# Reverse
str="AKHILA"
n=len(str)
for i in range(n):
    for j in range(n):
        print(f"{str[n-j-1]} ",end="")
    print()

#Name Triangle
str="AKHILA"
n=len(str)
for i in range(n):
    for j in range(i+1):
        print(f"{str[j]} ",end="")
    print()

# Same character in a row
str="AKHILA"
n=len(str)
for i in range(n):
    for j in range (i+1):
        print(f"{str[i]} ",end="")
    print()