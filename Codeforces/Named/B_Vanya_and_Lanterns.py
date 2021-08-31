n,k = map(int,input().split())
li = [int(i) for i in input().split()]
li.sort()
max_dist = 0
for i in range(n-1):
    d = li[i+1]-li[i]
    if d>max_dist:max_dist=d
max_dist /= 2
end = k-li[n-1]
front = li[0]-0
ans = max(max_dist,end,front)
print(f"{ans:.10f}")