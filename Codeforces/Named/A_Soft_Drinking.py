n,k,l,c,d,p,nl,np = map(int,input().split())
totalml = k*l
totalslices = c*d

print(min(totalml//nl,totalslices,p//np)//n)