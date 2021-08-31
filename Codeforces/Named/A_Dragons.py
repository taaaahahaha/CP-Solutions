s,n = map(int,input().split())
si = []
d = dict()
for i in range(n):
    a,b = map(int,input().split())
    if a in d.keys():
        d[a] += b
        # print("Hi",d[a])
    else:
        d[a] = b
    si.append(a)
si = list(set(si))
si.sort()
# print(si)
# print(d)
flag = True
for i in range(len(si)):
    if s>si[i]:
        s += d[si[i]]
    else:
        flag=False
        break

if flag:
    print("YES")
else:
    print("NO")