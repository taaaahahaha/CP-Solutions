a,b = map(int,input().split())
print((a-b+1) if (a-b)%10!=9 else print((a-b-1)))