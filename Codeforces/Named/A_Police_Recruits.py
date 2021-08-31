import math
import sys

ii = lambda: int(sys.stdin.readline())
imi = lambda: map(int,sys.stdin.readline().strip().split())
iil = lambda: [int(i) for i in sys.stdin.readline().split()]

MOD = 1000000007

n = ii()
li = iil()
sum = 0
min = 0
for i in range(len(li)):
    sum += li[i]
    if sum<min:min=sum
print(abs(min))
