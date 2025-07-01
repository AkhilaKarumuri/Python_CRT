s = input("Enter a string: ").lower()
res = ''
for char in s:
        if char not in res:
            res+= char + str(s.count(char))
        else:
            len(res) == len(s)
print(res)