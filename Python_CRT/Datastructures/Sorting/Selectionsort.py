def Selection(arr):
    print("Original Array:")
    print(arr)
    n=len(arr)
    for i in range(n):
        min_index=1
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
        print(arr)
Selection([5,3,6,8])