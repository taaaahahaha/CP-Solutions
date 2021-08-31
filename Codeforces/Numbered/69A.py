n = int(input())
sum=[0,0,0]
for i in range(n):
    li = [int(i) for i in input().split()]
    sum[0]+=li[0]
    sum[1]+=li[1]
    sum[2]+=li[2]
if sum==[0,0,0]:print("YES")
else:print("NO")
