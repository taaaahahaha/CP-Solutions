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

print(find_che(101))