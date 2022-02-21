ii = lambda: int(input())
imi = lambda: [int(i) for i in input().split()]

for _ in range(ii()):
    n = ii()
    if n<3:print(n)
    else:print(n//2+1)