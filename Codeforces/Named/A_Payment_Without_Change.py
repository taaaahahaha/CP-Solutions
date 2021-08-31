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
    a,b,n,s = imi()
    temp = s
    rem = s%n
    quo = s//n
    if quo>a:
        rem = temp-a*n
    # print(rem)
    if rem<=b:print("YES")
    else:print("NO")



for _ in range(ii()):
    solve()