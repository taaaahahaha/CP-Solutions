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
    li = iil()
    s = set(li)
    if len(s)==1:
        print("YES")
        print(li[0],li[1],li[2])
    elif len(s)==3:print("NO")
    else:
        maxnum = max(li)
        minnum = min(li)
        maxnumcount = li.count(maxnum)
        minnumcount = li.count(minnum)
        if minnumcount>maxnumcount:print("NO")
        else:
            print("YES")
            print(minnum,minnum,maxnum)

for _ in range(ii()):
    solve()