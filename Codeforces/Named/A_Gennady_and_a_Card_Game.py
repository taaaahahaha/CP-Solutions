t = [i for i in input()]
li = [i for i in input().split()]

found = False
for i in li:
    if i[0]==t[0] or i[1]==t[1]:
        found = True
        break
print("YES" if found else "NO")