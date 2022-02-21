ii = lambda: int(input())
imi = lambda: [int(i) for i in input().split()]

n1= ii()
n2 = ii()
if n1>n2:print(n1-n2)
else:print(n1+n2)