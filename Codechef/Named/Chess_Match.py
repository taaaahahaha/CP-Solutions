for _ in range(int(input())):
    n,a,b = map(int,input().strip().split())
    if n%2==0:
        n_a = (n//2)*2
        n_b = (n//2)*2
    else:
        n_a = ((n+1)//2)*2
        n_b = (n//2)*2
    print(360-(a+b - (n_a+n_b)))
    