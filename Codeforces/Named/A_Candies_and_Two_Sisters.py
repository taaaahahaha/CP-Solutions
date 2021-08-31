for i in range(int(input())):
    n = int(input())
    if n%2==0 and n>3:
        print(n//2-1)
    elif n>2:
        print(n//2)
    else:
        print(0)

