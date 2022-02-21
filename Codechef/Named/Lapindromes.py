ii = lambda: int(input())
imi = lambda: [int(i) for i in input().split()]

for _ in range(ii()):
    x = input()
    n = len(x)
    if n%2==0:
        s1 = list(x[:n//2])
        s2 = list(x[n//2:])
    else:
        s1 = list(x[:n//2])
        s2 = list(x[n//2+1:])
    s1.sort()
    s2.sort()
    if s1==s2:print("YES")
    else:print("NO")
