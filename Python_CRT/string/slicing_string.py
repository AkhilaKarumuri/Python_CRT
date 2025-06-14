# #Python Program
# str="Python Program"
# # Slicing the string
# print("Slicing the string:")
# print("str[1:6]:", str[1:6])  # Output: ython
# print("str[6:8]:", str[6:8])
# print("str[7:11]:",str[7:11])
# print("str[10:]:",str[10:])
# print(str[7:10])
# print(str[2:6])
# print(str[::-1])
# print(str[-9::-1])
# print(str[-1:-8:-1])
# print(str[-4:8:-1])

# Repetation Operator
# "$"*7
# str2="Students"
# print(str2*5)
# print(str2[1:3]*4)

# # Cancatenation operator
# a = "Hello" 
# b = "World"
# print(a + b)

# Input = input("Enter the string:")
# print(f"user entered String:{Input}")
# str_List=Input.split()
# str="".join(str_List)
# print(f"String without Spaces:{str_List}")

str1="Hi"
str2="Hello"
print(str1)
print(str2)
s=str1.join(str2)
print(s)

"""WAP to read string as input from the user print the string as a list of individual characters
Find the length of the string
Find the min element after converting string into list
Find the no.of.spaces present in the string without using any builtin functions/methods"""

"""WAp to read a the sentence as input from user and print the list of words from the sentence"""
sentence=input("Enter the sentence:")
List= sentence.split(" ")
print(List)
# print(list(sentence))