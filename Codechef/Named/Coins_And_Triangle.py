ii = lambda: int(input())
imi = lambda: [int(i) for i in input().split()]

for _ in range(ii()):
    n = ii()
    x = ((4+8*n)**0.5 - 1) // 2
    print(int(x))