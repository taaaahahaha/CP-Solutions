# Taaha Multani @ https://github.com/taaaahahaha

s = input()
t = ""
ans = ""
i=0
l=len(s)
while i<l:
    t+=s[i]
    if t=='.':
        ans+='0'
        t=''
    elif t=='-.':
        ans+='1'
        t=''    
    elif t=='--':
        ans+='2'
        t=''
    i+=1
print(ans)
