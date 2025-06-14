str1 = input()
result = ""
for ch in str1:
    if ch in 'AEIOUaeiou':
        result += '0'
    else:
        result += ch
print(result)