ii = lambda: int(input())
imi = lambda: [int(i) for i in input().split()]

n = ii()
if n%4==0:print(n+1)
else:print(n-1)