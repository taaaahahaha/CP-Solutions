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
    li = [2**i for i in range(1,n+1)]
    # print(li)
    s1,s2=0,0
    s1+=li[-1]
    for i in range(n//2-1):
        s1+=li[i]
    s2 = sum(li)-s1
    print(abs(s1-s2))
    

for _ in range(ii()):
    solve()