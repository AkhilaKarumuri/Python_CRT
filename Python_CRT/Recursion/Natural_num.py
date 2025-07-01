#Natural Numbers from 1-n
N=int(input("Enter the value of n:"))
def Naturalnum(N):
    if N==0:
        return
    Naturalnum(N-1)
    print(N)
Naturalnum(N)

#Natural Numbers from n to 1
def NaturalNum(N):
    if N!=0:
        print(N)
        return NaturalNum(N-1)
NaturalNum(N)