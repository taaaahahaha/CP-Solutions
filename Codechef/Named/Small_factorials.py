def fact(n):
    p = 1
    for i in range(2,n+1):
        p *= i
    return p

for _ in range(int(input())):
    print(fact(int(input())))