n = input()
li = [int(i) for i in input().split()]
arr = [li[0]]
c=0
for i in range(1,len(li)):
    min_point = min(arr)
    max_point = max(arr)
    if li[i]>max_point or li[i]<min_point:
        c+=1
    arr.append(li[i])

print(c)