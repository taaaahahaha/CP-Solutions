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


# def SOE(n):
#     prime = [True for i in range(n + 1)]
#     p = 2
#     while (p * p <= n):
#         if (prime[p] == True):
#                 for i in range(p * 2, n + 1, p):
#                     prime[i] = False
#         p += 1
#     prime[0]= False
#     prime[1]= False
#     li = []
#     for p in range(n + 1):
#         if prime[p]:
#             li.append(p),
#     return li


# n = ii()
# li = [(int(i)**0.5) for i in sys.stdin.readline().strip().split()]

# max_prime = max(li)
# soe_li = SOE(int(max_prime))

# for i in li:
#     if i in soe_li:print("YES")
#     else:print("NO")


n = ii()
li = iil()
for i in range(n):
    s = math.sqrt(li[i])
    if s-math.floor(s)==0:
        flag=1
        if li[i]==1:flag=0
        elif li[i]==4:flag=1
        elif li[i]%2==0:flag=0
        else:
            # print(s)
            for j in range(3,math.ceil(s),2):
                if j*j<=s:
                    if li[i]%j==0:
                        flag=0
                        break
                else:
                    break
        if flag:print("YES")
        else:print("NO")
    else:
        print("NO")