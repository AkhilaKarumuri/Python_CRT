n = int(input("Enter the number of n: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("* ", end="")
    print()

"""      *
       * *
     * * *
   * * * *"""
n = int(input("Enter the value of n:"))
for i in range(n):
    for j in range(n):
        if(j<=1):
            print(f"*")