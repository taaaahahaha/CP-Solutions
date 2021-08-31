n = int(input())
li = [int(i) for i in input().split()]
max = c =0
for i in range(1,len(li)):
    if li[i]>=li[i-1]:c+=1
    else:c=0
    if c>max:max=c
print(max+1)
