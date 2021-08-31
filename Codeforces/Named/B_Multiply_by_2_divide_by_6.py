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
    n = ii()
    c=0
    i = 0
    while n!=1:
        if n%6==0:
            n//=6
            i=0
        else:
            n*=2
            i+=1
        if i==10:
            c=-1
            break
        c+=1

    print(c)



for _ in range(ii()):
    solve()