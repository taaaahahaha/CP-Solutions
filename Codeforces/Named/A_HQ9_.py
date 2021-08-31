n = input()
li = ["H","Q","9"]
ans = False
for i in n:
    if i in li:
        ans = True
        break
if ans == True:print("YES")
else:print("NO")