"""WAPP to take the input from the user and print whether it is a prime or not using functions (return)"""
def prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
        else:
            return True
n=int(input("Enter the number:"))
if prime(n):
    print(f"{n} is a prime")
else:
    print(f"{n} is not prime")