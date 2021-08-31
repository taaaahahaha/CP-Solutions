import math
import sys

ii = lambda: int(sys.stdin.readline())
imi = lambda: map(int,sys.stdin.readline().strip().split())
iil = lambda: [int(i) for i in sys.stdin.readline().split()]
istr = lambda: sys.stdin.readline()
ims = lambda: sys.stdin.readline().split()
isl = lambda: [(i) for i in sys.stdin.readline().split()]

MOD = 1000000007

sum=0
for i in range(ii()):
    a,b = imi()
    if a>b : sum+=1
    elif a<b: sum-=1
if sum>0:print("Mishka")
elif sum<0:print("Chris")
else:print("Friendship is magic!^^")