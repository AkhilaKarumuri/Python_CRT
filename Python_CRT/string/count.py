"""WAPP to read a string as input from the user 
print count of uppercase letters
print count of lowercase letters
print the count of numeric values 
print the count of special characters"""
str=input("Enter the String: ")
Uppercase=0
lowercase=0
numeric=0
special=0
for ch in str:
    if ch.isupper():
        Uppercase+=1
    elif ch.islower():
        lowercase=+1
    elif ch.isnumeric():
        numeric+=1
    else:
        special+=1
print(f"The count Uppercase letters : {Uppercase}")
print(f"The count lowercase letters : {lowercase}")
print(f"The count numeric: {numeric}")
print(f"The count Special: {special}")