string = input("Enter a string: ")
length = len(string)
part_size = length // 3 
part1 = string[:part_size]
part2 = string[part_size:2*part_size]
part3 = string[2*part_size:]

print(f"First part: {part1}")
print(f"Second part: {part2}")
print(f"Third part: {part3}")