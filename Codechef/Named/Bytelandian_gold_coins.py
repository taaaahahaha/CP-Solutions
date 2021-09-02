# Taaha Multani @ https://github.com/taaaahahaha

d = dict()

def xd(n):
    if n<12: return n
    if n not in d:
        d[n] = max(n,xd(n//2)+xd(n//3)+xd(n//4))
    return d[n]


while True:
    try:
        n = int(input())
        print(xd(n))
    except:
        break

