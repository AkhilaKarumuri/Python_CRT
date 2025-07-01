t = int(input("enter the range: "))
for i in range(t):
    values = input().split()
    a = int(values[0])
    b = int(values[1])
    c = int(values[2])
    x = int(values[3])
    y = int(values[4])

    if a+b+c != x+y:
        print("No")
    elif max(x,y) > max (a+b+c,c+b):
        print("No")
    else:
        print("Yes")