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
    if n%2==0:
        print(n//2)
    else:
        print(n//2+1)
   

for _ in range(ii()):
    solve()