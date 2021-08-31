n = int(input())
li = []
d = dict()
for i in range(n):
    s = input()
    if s in d.keys():
        d[s]+=1
    else:
        d[s]=0
    if d[s]==0:print("OK")
    else:
        print(s+str(d[s]))

        