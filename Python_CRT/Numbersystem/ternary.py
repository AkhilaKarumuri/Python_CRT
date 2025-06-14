Num = int(input("Enter a number: "))
if Num < 0:
    print("f{Num} is negative")
elif Num >0 :
    print(f"{Num} is positive")
else:
    print("The number is zero")
Res= "Positive" if (Num > 0) else "Negative"
print (f"{Num} is a {Res}")