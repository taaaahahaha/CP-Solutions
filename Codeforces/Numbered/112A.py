s1 = list(input().lower())
s2 = list(input().lower())

i=0
while True:
    if ord(s1[i])>ord(s2[i]):
        print("1")
        break
    elif ord(s1[i])<ord(s2[i]):
        print("-1")
        break
    elif i == len(s1)-1:
        print("0")
        break
    i+=1
        

