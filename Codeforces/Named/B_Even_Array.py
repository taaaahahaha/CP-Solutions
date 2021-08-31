import math
import sys

ii = lambda: int(sys.stdin.readline())
imi = lambda: map(int,sys.stdin.readline().strip().split())
iil = lambda: [int(i) for i in sys.stdin.readline().split()]
istr = lambda: sys.stdin.readline()
ims = lambda: sys.stdin.readline().split()
isl = lambda: [(i) for i in sys.stdin.readline().split()]

MOD = 1000000007

for _ in range(ii()):
    ans = True
    n = ii()
    li = iil()
    c_e,c_o = 0,0
    for i in range(len(li)):
        if li[i]%2==0:c_e+=1
        else:c_o+=1
    if n%2==0:
        if c_e != c_o: ans = False
    else:
        if c_e-1 != c_o: ans = False

    if ans:
        c=0
        for i in range(n):
            if i%2==0:
                if li[i]%2!=0:c+=1
        print(c)
    else:
        print(-1)
