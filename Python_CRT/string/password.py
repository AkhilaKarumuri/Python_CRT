"""WAPP to take password as input from the user and check whether it is valid or not"""

password = input("Enter your password: ")
valid = True
if len(password) < 8:
    valid = False
if password.isdigit() or password.isalpha():
    valid = False
if valid:
    print("Password is valid!")
else:
    print("Password is invalid!")