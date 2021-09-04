def isTriangle(a,b,c):
    if a+b>c and b+c>a and a+c>b:return True
    return False


def solve():
    a,b,c,d = map(int,input().split())
    # x=[i for i in range(a,b+1)]
    # y=[i for i in range(b,c+1)]
    # z=[i for i in range(c,d+1)]

    # found = False

    # y = (b+c)//2
    # x = b
    # z = c

    # print(x,y,z)

    print(b,c,c)



for _ in range(int(input())):
    solve()