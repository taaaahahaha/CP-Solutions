a,b = map(int,input().split())
while a!=0 and b!=0 and min(a,b)*2<=max(a,b):
    if a>=2*b: a %= 2*b
    else: b %= 2*a
print(a,b)
