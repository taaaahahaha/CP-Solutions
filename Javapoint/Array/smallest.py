arr = [1,2,3,4,5,6,7,8,9,10,11,12,13]
min=arr[0]
for i in range(len(arr)):
    if arr[i] <= min: min=arr[i]
print(min)