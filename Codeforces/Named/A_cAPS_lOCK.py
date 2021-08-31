s = input()
if len(s)==1:print(s.upper() if s.islower() else s.lower())
elif s.isupper() or s[1:].isupper():
    li = list(s)
    for i in range(len(li)):
        if li[i].islower():li[i]=li[i].upper()
        else:li[i]=li[i].lower()
    print(''.join(li))
else:
    print(s)
        