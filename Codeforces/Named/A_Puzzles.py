n,k=map(int,input().split())
li = [int(i) for i in input().split()]
li.sort()
min=li[n-1]-li[0]
for i in range(1,k-n+1):
    sum = li[n+i-1]-li[i]
    if sum<min:min=sum
print(min)