n = int(input())

home = []
guest = []
c = 0

for i in range(n):
    h,g = map(int,input().split())
    if h in guest:
        c+=guest.count(h)
    if g in home:
        c+=home.count(g)
    # print(i,c)
    home.append(h)
    guest.append(g)
print(c)