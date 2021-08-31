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
    linew = li.copy()
    li.sort()
    if li[0]!=li[1]:print(linew.index(li[0])+1)
    else:print(linew.index(li[-1])+1)
   

for _ in range(ii()):
    solve()