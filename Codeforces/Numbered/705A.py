s="I hate "
n=int(input())
for i in range(2,n+1):
    if i%2!=0: s+= "that I hate "
    else : s+="that I love "
s+="it"
print(s)