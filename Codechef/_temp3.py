def fact(n):
    if n<2:return 1
    else:return n*fact(n-1)


for _ in range(int(input())):
    n,k = map(int,input().split())
    prod = 1
    for i in range(n-1,n-k,-1):
        prod *= i
    print(prod//fact(k-1))
    # print(prod)

# for _ in range(int(input())):
#     n,k = map(int,input().split())
#     n -= 1
#     k -= 1
#     print(fact(n)//(fact(k)*fact(n-k)))