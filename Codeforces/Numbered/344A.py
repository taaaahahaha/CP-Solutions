n = int(input())
c = 1
ans = int(input())
for i in range(n-1):
    x = int(input())
    if x == ans :
        continue
    else:
        c += 1
        ans = x
print(c)
