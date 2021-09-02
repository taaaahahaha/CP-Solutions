for _ in range(int(input())):
    n = int(input())
    li = [int(i) for i in input().split()]
    li.sort()
    d = li[1]-li[0]
    for i in range(2,len(li)):
        if li[i]-li[i-1]<d:d=li[i]-li[i-1]
    print(d)