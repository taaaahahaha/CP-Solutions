# Taaha Multani @ https://github.com/taaaahahaha

t = int(input())
for i in range(t):
    x, y = map(int,input().strip().split())  #n^2-n+1 diagonal element 1,3,7,13
    a = max(x,y)
    diag = a**2 - a +1
    if(x-y==0):print(diag)
    else:
        if(a%2==0):
            print(diag+(x-y))
        else:
            print(diag+(y-x))
    