ii = lambda: int(input())
imi = lambda: [int(i) for i in input().split()]

for _ in range(int(input())):
    li = imi()
    if sum(li)==180:print("YES")
    else:print("NO")