'''5. Calculate the Average of Numbers in a Given List Write a program to calculate and return the average (mean) of a list of numbers (integers or floats). If the list is empty, handle the case with a suitable message.'''

numbers = [10, 20, 30, 40, 50]
if numbers:
    average = sum(numbers) / len(numbers)
    print(f"Average: {average}")
else:
    print("The list is empty.")