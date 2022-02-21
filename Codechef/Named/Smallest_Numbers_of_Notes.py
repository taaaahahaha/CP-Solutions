ii = lambda: int(input())
imi = lambda: [int(i) for i in input().split()]

li = [100,50,10,5,2,1]

for _ in range(ii()):
    c=0
    n = ii()
    for i in li:
        c += n//i
        n = n%i
    print(c)
