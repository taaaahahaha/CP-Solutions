n = int(input())
li = [int(i) for i in input().split()]

s1,s2=0,0
i=0 

while i<n:
    a,b = li[0],li[n-1-i]
    if a>b:
        x = li.pop(0)
    else:
        x = li.pop()
    
    if i%2==0:s1+=x
    else:s2+=x

    i+=1

print(s1,s2)
    