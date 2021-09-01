arr = [1,2,3,4,5,6,7,1,2,3,4]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            print(arr[j])