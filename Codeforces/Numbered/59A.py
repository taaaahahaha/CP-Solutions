w = list(input())
s,c=0,0
for i in range(len(w)):
    if w[i]>='a' and w[i]<='z': s += 1
    else : c +=1
str = ''.join(w)
if(c>s):print(str.upper())
else:print(str.lower())