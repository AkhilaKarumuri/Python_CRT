"""WAPP to read the length of the string as input from the user and print all the binary strings of length n"""
def generate_binary_no_backtrack(n):
    result = '0' * n
    print(result)
generate_binary_no_backtrack(3)
print("With BackTracking")
def generate_binary_backtrack(n,current=""):
    if len(current) == n:
        print(current)
        return
    generate_binary_backtrack(n,current+'0')
    generate_binary_backtrack(n,current+'1')
generate_binary_backtrack(3)