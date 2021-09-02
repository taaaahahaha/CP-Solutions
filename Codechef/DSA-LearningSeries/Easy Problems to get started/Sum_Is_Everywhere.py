n = int(input())
se,so = 0,0
for i in range(1,2*n+1):
    if i%2!=0:so+=i
    else:se+=i
print(so,se)