l,r = map(int,input().split())
li = []
for i in range(l,r+1):
    if i%2!=0:
        li.append(i)
print(" ".join([str(i) for i in li]))