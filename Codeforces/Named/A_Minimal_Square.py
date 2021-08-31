import math
import sys

ii = lambda: int(sys.stdin.readline())
imi = lambda: map(int,sys.stdin.readline().strip().split())
iil = lambda: [int(i) for i in sys.stdin.readline().split()]
istr = lambda: sys.stdin.readline()
ims = lambda: sys.stdin.readline().split()
isl = lambda: [(i) for i in sys.stdin.readline().split()]

MOD = 1000000007

n = ii()
for _ in range(n):
    a,b = imi()
    a,b = min(a,b),max(a,b)
    if 2*a<b:
        area = b**2
    else:
        area = (2*a)**2
    print(area)
   
