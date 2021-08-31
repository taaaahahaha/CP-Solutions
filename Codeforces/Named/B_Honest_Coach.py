import math
import sys

ii = lambda: int(sys.stdin.readline())
imi = lambda: map(int,sys.stdin.readline().strip().split())
iil = lambda: [int(i) for i in sys.stdin.readline().split()]
istr = lambda: sys.stdin.readline()
ims = lambda: sys.stdin.readline().split()
isl = lambda: [(i) for i in sys.stdin.readline().split()]

MOD = 1000000007

for _ in range(int(input())):
    n = ii()
    li = iil()
    li.sort()
    min_d = li[1]-li[0]
    for i in range(1,n-1):
        d = li[i+1]-li[i]
        if d<min_d:min_d=d

    print(min_d)