n,h = map(int,input().strip().split())
li = [int(i) for i in input().split()]
w = 0
for e in li:
    if e>h : w+=2
    else: w+=1
print(w)

