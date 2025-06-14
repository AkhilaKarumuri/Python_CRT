"""WAP to read the string as input from the user
Reverse the string
Convert the string into lowercase
Convert the string into uppercase
Convert the characters of string to lower case if it is in upper case & convert to uppercase if it is in lower case
Check if the string is starting with the letter A 
Print the count of character A from the given string & replace all letter P to letter J"""
str=input("Enter the String:")
print(str[::-1])
print(str.lower())
print(str.upper())
print(str.swapcase())
print(str.startswith('A'))
print(str.count('P'))
str=str.lower()
print(str.replace('p','j'))

print(str.capitalize())
print(str.title())
print(str.casefold())
print(str.startswith('P'))
print(str.find('o'))
print("Hi".center(15,"*"))