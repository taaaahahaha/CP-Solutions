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
    n = ii()
    li = iil()
    if sum(li)%2!=0:print("YES")
    else:
        found = False
        no = ne = 0
        for i in li:
            if i%2==0:ne+=1
            if i%2!=0:no+=1
            if ne!=0 and no!=0:
                found  = True
                break
        if found:print("YES")
        else:print("NO")
   

for _ in range(ii()):
    solve()