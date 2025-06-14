Num = int(input("Enter the number : "))
if Num >= -9 and Num <=9:
    print(f"{Num} is Digit")
else:
    print(f"{Num} is Number")
# using Ternary
Res= "Digit" if Num<= -9 and Num>=9 else "Number"
print(f"{Num} is {Res}")