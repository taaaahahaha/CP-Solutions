arr = [1,2,3,4,5,6,7,8,9,10,11,12,13]
n = int(input())
for i in range(n):
    temp = arr[len(arr)-1]
    for j in range(len(arr)-1,-1,-1):
        arr[j] = arr[j-1]
    arr[0] = temp
print(arr)
        