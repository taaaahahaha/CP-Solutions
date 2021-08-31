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
    x = int(str(n)[0])
    s = 10*(x-1)
    l = len(str(n))

    s+= (l*(l+1))//2
    print(s)

    
   

for _ in range(ii()):
    solve()