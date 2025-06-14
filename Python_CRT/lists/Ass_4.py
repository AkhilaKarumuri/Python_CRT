'''4. Swap the First and Last Value of the Given List
Write a program that swaps the first and last elements of a given list and returns the updated list. The list may contain elements of any data type.'''

list = [1, 2, 3, 4, 5]
list[0], list[-1] = list[-1], list[0]
print(list) 