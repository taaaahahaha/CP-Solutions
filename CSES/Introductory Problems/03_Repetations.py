# Taaha Multani @ https://github.com/taaaahahaha

s=input()
s1=s[0]
count=0
res=0
for x in s+"Z":
    if x==s1:
        count += 1
    else:
        res=max(res,count)
        count=1
        s1=x
print(res)