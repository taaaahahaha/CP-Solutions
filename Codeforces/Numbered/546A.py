k,n,w = map(int,input().strip().split())
ans = (w*k*(w+1)//2) - n
if ans>=0:print(ans)
else:print("0")