# Taaha Multani @ https://github.com/taaaahahaha

for _ in range(int(input())):
    d,x,y,z = map(int,input().strip().split())
    a = 7*x
    b = (d*y) + (z*(7-d))
    print(a if a>b else b)