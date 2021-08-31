import math
import sys

ii = lambda: int(sys.stdin.readline())
imi = lambda: map(int,sys.stdin.readline().strip().split())
iil = lambda: [int(i) for i in sys.stdin.readline().split()]
istr = lambda: sys.stdin.readline()
ims = lambda: sys.stdin.readline().split()
isl = lambda: [(i) for i in sys.stdin.readline().split()]

MOD = 1000000007

n = ii()
li = iil()

ind_1 = []
ind_2 = []
ind_3 = []

for i in range(len(li)):
    if li[i]==1:
        ind_1.append(str(i+1))
    elif li[i]==2:
        ind_2.append(str(i+1))
    else:
        ind_3.append(str(i+1))

m = min(len(ind_1),len(ind_2),len(ind_3))

print(m)
for i in range(m):
    print(ind_1[i],ind_2[i],ind_3[i])