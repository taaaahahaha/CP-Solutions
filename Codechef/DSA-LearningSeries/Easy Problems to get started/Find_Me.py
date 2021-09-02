n,k = map(int,input().strip().split())
li = [int(i) for i in input().split()]
a = -1
for i in li:
    if i==k:
        a=1
        break
print(a)