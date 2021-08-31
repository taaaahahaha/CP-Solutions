a,b = map(int,input().strip().split())
count = 0
while(a<=b):
    count += 1
    a=3*a
    b=2*b
print(count) 