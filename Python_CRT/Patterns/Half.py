Str="AKHIL"
Length=len(Str)
mid=Length//2
for i in range(Length):
    for j in range(Length):
        if i == mid :
            print(Str[j], end=" ")
        elif j==mid:
            print(Str[i], end=" ")
        else:
            print("  ", end="") 
    print()