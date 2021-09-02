n = int(input())
c = 0
li = []
for i in range(1,n+1):
    if n%i==0:
        li.append(i)
        c+=1
print(c)
print(' '.join([str(i) for i in li]))