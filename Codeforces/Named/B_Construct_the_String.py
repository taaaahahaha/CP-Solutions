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
    ogletters = "abcdefghijklmnopqrstuvwxyz"
    letters = "abcdefghijklmnopqrstuvwxyz"
    n,a,b = imi()

    w = letters[:b]

    while len(w)<n:
        w+=w
    
    w = w[:n]
    print(w)











    
   

for _ in range(ii()):
    solve()