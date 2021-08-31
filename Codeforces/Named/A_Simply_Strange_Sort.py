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


def f(x,li):
    if li[x]>li[x+1]:
        temp = li[x]
        li[x]=li[x+1]
        li[x+1]=temp






def solve():
    n = ii()
    li = iil()
    temp_list = li.copy()
    temp_list.sort()
    c=0
    while li!=temp_list:
        # print(li)

        if c%2==0:
            # print("h")
            permlist = list(range(0,n-1,2))
            # print(permlist) 
            for i in permlist:
                f(i,li)



        else:
            # print("Y")
            permlist = list(range(1,n-1,2))
            # print(permlist)
            for i in permlist:
                f(i,li)

        c+=1
    print(c)
   

for _ in range(ii()):
    solve()