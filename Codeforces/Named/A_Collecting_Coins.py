import math
import sys

ii = lambda: int(sys.stdin.readline())
imi = lambda: map(int,sys.stdin.readline().strip().split())
iil = lambda: [int(i) for i in sys.stdin.readline().split()]
istr = lambda: sys.stdin.readline()
ims = lambda: sys.stdin.readline().split()
isl = lambda: [(i) for i in sys.stdin.readline().split()]

MOD = 1000000007

def solve():
    a,b,c,n = imi()
    s=0
    for i in [a,b,c]:
        s+=max(a,b,c)-i
    # print(s,n)
    if s<=n and (n-s)%3==0:print("YES")
    else:print("NO")

   

for _ in range(ii()):
    solve()