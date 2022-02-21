ii = lambda: int(input())
imi = lambda: [int(i) for i in input().split()]



for _ in range(int(input())):
    n = ii()
    if n<1500:
        hra = 0.1*n
        da = 0.9*n
    else:
        hra = 500
        da = 0.98*n
    gross_salaray = n + hra + da
    print(gross_salaray)