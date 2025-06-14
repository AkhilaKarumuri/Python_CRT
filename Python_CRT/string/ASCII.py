"""WAPP to print upper case alphabets from A-Z including their ASCII values"""
for i in range(1,27):
    print(chr(i+64),"-",i+64)
print("-----------")
for i in range(1,27):
    print(chr(i+96),"-",i+96)

"""WAPP to take the char as input from the user and print it's ASCII value"""
char=input()
ascii=ord(char)
print(ascii)