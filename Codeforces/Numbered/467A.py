c=0
for i in range(int(input())):
    a,b = map(int,input().strip().split())
    if b-a>1 : c+=1
print(c)