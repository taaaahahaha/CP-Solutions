# Taaha Multani @ https://github.com/taaaahahaha
import math
import sys

ii = lambda: int(sys.stdin.readline().strip())
imi = lambda: map(int,sys.stdin.readline().strip().split())
iil = lambda: [int(i) for i in sys.stdin.readline().strip().split()]
istr = lambda: sys.stdin.readline().strip()
ims = lambda: sys.stdin.readline().strip().split()
isl = lambda: [(i) for i in sys.stdin.readline().strip().split()]

MOD = 1000000007

def solve():
    n = ii()
    li = iil() 
    c1 = c2 = 0
    for i in li:
        if i==2:c2+=1
        else:c1+=1
    s = 2*c2 + c1
    if c1==0:
        if c2%2==0:print("YES")
        else:print("NO")
    elif c2==0:
        if c1%2==0:print("YES")
        else:print("NO")
    else:
        if (2*c2+c1)%2==0:
            print("YES")

        else:print("NO")
   

for _ in range(ii()):
    solve()