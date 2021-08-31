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
    n,k,s = imi()
    l = n+k-1
    li = [2*i-1 for i in range(1,n+1)]
    print((s-sum(li))//(k-1))
    
   

for _ in range(ii()):
    solve()