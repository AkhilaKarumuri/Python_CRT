#String---->Group of characters enclosed in single or double quotes
#Types of declaring strings
#single quotes
Str1='Good Morning'
print(type(Str1))
print(Str1)
#double quotes
Str2="Good Morning"
print(type(Str2))
print(Str2)
#triple quotes
Str3="""Good Morning
I am learning Python"""
print(type(Str3))
print(Str3)
#single triple quotes
Str4='''Good Morning 
I am learning Python'''
print(type(Str4))
print(Str4)
#single quotes highlighting double quotes
Str5='''Good Morning I am learning "Python"'''
print(type(Str5))
print(Str5)

a=10
b='10'
print(a is b)  # False, different types

str="Python"
print("The length of the string is:", len(str))
#Accessing without using index
for i in str:
    print(i, end=' ')
print()  
#Accessing using index
for i in range(len(str)):
    print(str[i], end=' ')

str1="Python"
str1[4]="i"
for c in str1:
    print(c)