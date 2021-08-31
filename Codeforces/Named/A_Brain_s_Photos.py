n,m = map(int,input().split())
color = False
li = []
baw = ['W','B','G']
for i in range(n):
    l = set([j for j in input().split()])
    for j in l:
        if j not in baw:
            color = True
            break
if color:print("#Color")
else:print("#Black&White")
