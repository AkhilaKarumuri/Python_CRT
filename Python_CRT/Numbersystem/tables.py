num = int(input("Enter the no.of tables:"))
for i in range (1,num+1):
    print(f"Multiplication table of {i}:")
    for j in range(1,11):
        print(f"{i}x{j}=",i*j)
    print()