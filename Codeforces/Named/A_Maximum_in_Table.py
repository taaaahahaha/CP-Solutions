n = int(input())
def x(r,c):
    if r==1 or c==1:
        return 1
    else:
        return x(r,c-1)+x(r-1,c)

print(x(n,n))
    