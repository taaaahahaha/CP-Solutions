n,k = map(int,input().split())
li = [int(i) for i in input().split()]
c=0
ind=0
for i in range(len(li)-1):
    if li[i]>li[i+1]:
        c+=1
        ind = i
ans = c*n
last = li.pop()
print(ans+(last-1))