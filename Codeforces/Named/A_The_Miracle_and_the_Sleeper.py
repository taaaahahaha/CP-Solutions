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
    l,r = imi()
    
    d = r//2+1
    if d>=l:
        print(r%(d))
    else:print(r%l)

for _ in range(ii()):
    solve()