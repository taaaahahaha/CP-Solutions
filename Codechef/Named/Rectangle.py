ii = lambda: int(input())
imi = lambda: [int(i) for i in input().split()]

for _ in range(ii()):
    li = imi()
    li.sort()
    if li[0]+li[3]==li[1]+li[2]:print("YES")
    else:print("NO")