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
    n,k = imi()
    li = iil()
    li2 = li.copy()
    li2.sort()

    s_n=0
    for i in li2:
        if i<0 and k!=0:
            s_n+=abs(i)
            k-=1
    
    s_p=0
    for i in li:
        if i>0:s_p+=i
    
    # print(li)
    print(s_n+s_p)

   

for _ in range(ii()):
    solve()