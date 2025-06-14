"""WAP to read the list of characters as input from the user and convert it into a word and print it"""

size=int(input("Enter the length of the list:"))
char_list=[]
for i in range (size):
    ch=input(f"Enter the character at {i}th index:")
    char_list.append(ch)
print(char_list)
str="".join(char_list)
print(str)