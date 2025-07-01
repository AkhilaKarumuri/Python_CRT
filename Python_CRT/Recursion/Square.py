# write py prog to print square num from n to 1
def square(N):
    if N==0:
        return
    print(N*N)
    square(N-1)
square(5)
# write py prog to print prime num from 1 to n

# write py prog to print prime num from n to 1

# write py prog to print square num from 1 to n
def square(N):
    if N==0:
        return
    square(N-1)
    print(N*N)
square(5)