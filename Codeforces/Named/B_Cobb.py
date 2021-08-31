for _ in range(int(input())):
    n,k = map(int,input().strip().split())
    li = [int(i) for i in input().split()]
    m = ((0+0)*(1+1)) - k*(li[0] | li[1])
    for i in range(n):
        for j in range(i+1,n):
            ans = ((i+1)*(j+1)) - k*(li[i] | li[j])
            if ans>m:m=ans
    print(m)