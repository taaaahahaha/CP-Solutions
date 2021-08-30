n,k = map(int,input().strip().split())
count = 0
for i in range(n):
    if int(input())%k == 0: count += 1
print(count)