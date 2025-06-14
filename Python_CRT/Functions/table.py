# def table(num):
#     for i in range (1,11):
#         print(f"{num}x{i}=",num*i)
# table(5)

# print---> 1-n tables
def tables(n):
    for i in range(1,n+1):
        print(f"The multiplication table of {i} is: ")
        for j in range(1,11):
            print(f"{i}x{j} = {i*j}")
    print()
tables(3)