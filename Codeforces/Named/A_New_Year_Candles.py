a,b = map(int,input().split())
s=0
while a>=b:
    s+=b
    a-=b
    a+=1
print(s+a)