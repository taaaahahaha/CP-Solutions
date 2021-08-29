def chefora(n):
    n = str(n)
    d = len(n)
    temp=0
    for i in range(0,d):
        temp+= (int(n[i]) * (10**i))
    if d%2!=0 and int(n)==temp:return True
    else:return False


def find_che(n):
    while True:
        if chefora(n): return n
        n+=1

for _ in range(int(input())):
    l,r = map(int,input().strip().split())

    AL = find_che(l)
    
    p = 1
    t=l+1
    for i in range(l+1,r+1):
        t = find_che(t+1)
        p *= AL**t
    print(p%(10**9 + 7))
