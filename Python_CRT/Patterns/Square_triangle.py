"""1
   2 3
   4 5 6
   7 8 9 10"""
n=int(input())
for i in range(1,n+1):
    for j in range(i,i+1):
            print(j,end="")
    i+=1
    print()
"""
1
4 9
16 25 36
49 64 81 100"""