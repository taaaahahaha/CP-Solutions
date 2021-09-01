arr = [5,6,3,4,8,2,1,44,98,76]
print(arr)
print(sorted(arr)[::-1])


for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]<arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print(arr)