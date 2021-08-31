s = input()[1:-1]
li = ([i.strip() for i in s.split(',')])
if li[0]=='':print(0)
else:print(len(set(li)))