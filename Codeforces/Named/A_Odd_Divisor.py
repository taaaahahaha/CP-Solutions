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
    n = ii()
    if (bin(n)).count('1')==1:print("NO")
    else:print("YES")


for _ in range(ii()):
    solve()



# 2 x
# 3 y
# 4 x
# 5 y
# 6 y
# 7 y
# 8 x
# 9 y
# 10 y

# 11 y
# 12 y
# 13 y
# v4 y
# 15 y
# 16 n
# v7 y
# 18 y
# 19 y
# 20 y

#2 4 8 16
#10 100 1000 10000