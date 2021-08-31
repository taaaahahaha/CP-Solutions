li = []
for i in range(3):
    n = int(input())
    li.append(n)
a = li[0]+li[1]+li[2]
b = li[0]*li[1]*li[2]
c = (li[0]+li[1])*li[2] 
d = li[0]*(li[1]+li[2])
print(max(a,b,c,d))
