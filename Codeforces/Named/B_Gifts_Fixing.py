import math
import sys

ii = lambda: int(sys.stdin.readline())
imi = lambda: map(int,sys.stdin.readline().strip().split())
iil = lambda: [int(i) for i in sys.stdin.readline().split()]
istr = lambda: sys.stdin.readline()
ims = lambda: sys.stdin.readline().split()
isl = lambda: [(i) for i in sys.stdin.readline().split()]

MOD = 1000000007

for _ in range(ii()):
    n = ii()
    li1 = iil()
    li2 = iil()
    min_li1 = min(li1)
    min_li2 = min(li2)
    li1 = [i-min_li1 for i in li1]
    li2 = [i-min_li2 for i in li2]
    sum = 0
    for i in range(n):
        a,b = min(li1[i],li2[i]),max(li1[i],li2[i])
        sum+=a
        b-=a
        sum+=b
    print(sum)

