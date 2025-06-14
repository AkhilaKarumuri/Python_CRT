'''6. Print Sum of Negative Numbers, Positive Even Numbers, and Positive Odd Numbers in a List
Write a program that takes a list of integers and calculates:

* The sum of all negative numbers
* The sum of all positive even numbers
* The sum of all positive odd numbers
  Display each sum clearly.'''

n=(int(input("Enter the size of the list: ")))
num=[]
for i in range(n):
    temp=int(input(f"Enter element {i}: "))
    num.append(temp)
sum_negative = 0
sum_positive_even = 0
sum_positive_odd = 0
for number in num:
    if number < 0:
        sum_negative += number
    elif number > 0:
        if number % 2 == 0:
            sum_positive_even += number
        else:
            sum_positive_odd += number
print("The sum of negative numbers is:", sum_negative)
print("The sum of positive even numbers is:", sum_positive_even)
print("The sum of positive odd numbers is:", sum_positive_odd)