t= int(input())
for i in range(t):
    n= int(input())
    inputs=input().split()
    item=[]
    for i in range(n):
        item.append(int(inputs[i]))
    max_count=0
    item_type=item[0]
    j=0
    while j<n: