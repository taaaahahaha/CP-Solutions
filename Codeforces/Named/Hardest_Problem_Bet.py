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
    a,b,c = imi()
    maxnum = min(a,b,c)
    if maxnum==a:
        print("Draw")
    elif maxnum==b:
        print('Bob')
    else:
        print('Alice')
   

for _ in range(ii()):
    solve()