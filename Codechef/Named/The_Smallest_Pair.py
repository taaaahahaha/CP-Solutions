ii = lambda: int(input())
imi = lambda: [int(i) for i in input().split()]

for _ in range(ii()):
    n = ii()
    li = imi()
    li.sort()
    print(li[0]+li[1])