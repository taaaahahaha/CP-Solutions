ii = lambda: int(input())
imi = lambda: [int(i) for i in input().split()]

for _ in range(int(input())):
    n,w = map(int,input().split())
    li = imi()
    li.sort(reverse=True)
    # print(li)
    for i in li:
        w -= i
        n-=1
        if w<=0:
            print(n)
            break
