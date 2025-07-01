#Method call
N=int(input("Enter the value of n:"))
i=0
def Naturalnum(N,i):
    i=i+1
    if N==0:
        return
    Naturalnum(N-1,i)
    print(f"{i} method call")
Naturalnum(N,i)