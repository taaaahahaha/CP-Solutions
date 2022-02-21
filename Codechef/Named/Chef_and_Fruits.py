ii = lambda: int(input())
imi = lambda: [int(i) for i in input().split()]

import math

for _ in range(ii()):
    n,m,k = imi()
    diff = abs(n-m)
    x = k-diff
    if x<0:print(abs(x))
    elif x==0 or x%2==0:print(0)
    else:print(1)
