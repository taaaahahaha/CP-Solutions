x, y = map(float,input().strip().split())
if x%5==0 and x+0.5<=y: 
    ans = y-x-0.5
else: 
    ans = y
print(ans)