'''Problem:
Given a list of integers that may contain duplicates.
sort the list in ascending order and remove all duplicates.

Input:
A List of integers arr with length n (1 _< n <1000)
Output:
Sorted list with unique elements only
-------------------------------------
Input: [4,2,2,8,4,6]
Output: [2,4,6,8]'''
n=int(input("Enter the size of the list: "))
List=[]
for i in range (n) :
    temp=int(input(f"Enter the element at {i}th index :"))
    List.append(temp)
print(List)
unique_List=list(set(List))
# unique_List.sort()
Sorted_List = sorted(unique_List)
print(unique_List)
print(Sorted_List)