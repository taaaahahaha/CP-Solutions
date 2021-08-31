n,k = map(int,input().strip().split())
li = [int(i) for i in input().split()]
count = 0
for _ in range(n):
    if li[_] >= li[k-1] and li[_]>0: count += 1
print(count)
