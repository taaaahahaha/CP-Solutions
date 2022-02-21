ii = lambda: int(input())
imi = lambda: [int(i) for i in input().split()]

# Max=2048

for _ in range(ii()):
    n = ii()
    c = 0
    for i in range(11,0,-1):
        c += n//(2**i)
        n = n%(2**i)
    print(c+n)