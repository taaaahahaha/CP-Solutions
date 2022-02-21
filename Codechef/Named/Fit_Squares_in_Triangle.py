ii = lambda: int(input())
imi = lambda: [int(i) for i in input().split()]

for _ in range(ii()):
    n = ii()
    maxlen = n//2
    print(maxlen)
    # if maxlen<2:print("0")
    # else:
    #     if maxlen%2!=0:
    #         maxlen -= 1
    #     print(maxlen**2//4)