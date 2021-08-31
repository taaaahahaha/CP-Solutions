# Taaha Multani @ https://github.com/taaaahahaha

for _ in range(int(input())):
    
    n = int(input())
    d = dict()
    for __ in range(3*n):
        a,b = input().split()
        b = int(b)
        if a in d.keys():
            d[a]=d[a]+b
        else:
            d[a] = b
    values = d.values()
    li = sorted(values)
    print(" ".join([str(x) for x in li]))