n = int(input())
s = ''.join(list(set(str(n))))
c1=0
c2=0
if s=='47' or s=='74' : c1+=1
x = [4,7,44,77,47,74,447,474,774,747,477,744]
for i in x:
    if n%i==0 : c2+=1
if (c1>=1 or c2>=1):print("YES")
else:print("NO")
