x = 0
ans = 0
for i in range(int(input())):
    a,b=map(int,input().strip().split())
    x = x-a+b
    if x>ans : ans=x
print(ans)