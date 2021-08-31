n,k=map(int,input().split())
t = 240-k
c=0
i=1
sum=0
while i<=n:
    sum += 5*i
    if sum>t:break
    i += 1
    c+= 1
print(c)