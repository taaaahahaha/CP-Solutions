ii = lambda: int(input())
imi = lambda: [int(i) for i in input().split()]


li=[]
for _ in range(ii()):
    li.append(ii())

li.sort()
n=len(li)
ans = 0
for i in range(n):
    ans = max(ans,(n-i)*li[i])

print(ans)
