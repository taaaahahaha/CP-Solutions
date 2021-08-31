n = int(input())
l = [int(i) for i in input().split()]
li = []
for i in range(1,n+1):
    li.append(l.index(i)+1)
li = [str(i) for i in li]
print(' '.join(li))