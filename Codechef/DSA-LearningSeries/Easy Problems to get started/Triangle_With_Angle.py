li = [int(i) for i in input().split()]
if sum(li) == 180 and li[0]>0 and li[1]>0 and li[2]>0:print("YES")
else:print("NO")