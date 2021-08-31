n , t = map(int,input().strip().split())
w = input()
while t:
    w = w.replace("BG","GB")
    t-=1
print(w)
