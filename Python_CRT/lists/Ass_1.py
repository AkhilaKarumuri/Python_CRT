'''1. Count the Number of Null Elements in a List
Write a program that takes a list containing various data types, including None values. Your task is to count how many None values are present in the list and return the count.'''

my_list=['3.4','none','2','hello','none','python']
count=0
for i in my_list:
    if i == 'none':
        count+=1
print("The no.of values in the list:"f"{count}")