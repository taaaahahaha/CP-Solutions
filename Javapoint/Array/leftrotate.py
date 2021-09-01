arr = [1,2,3,4,5,6,7,8,9]
n = int(input())
for j in range(n):
    temp = arr[0]
    for i in range(len(arr)):
        if i==len(arr)-1:
            arr[i]=temp
        else:
            arr[i] = arr[i+1]
print(arr)
