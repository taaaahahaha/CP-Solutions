for i in range(int(input())):
    s = input()
    l = list(s)
    f=1
    if len(s)==0:
        print("Error")
    elif s[:2]=="</" and s[len(l)-1]==">":
        for i in range(2,len(l)-1):
            if l[i].isalpha() and l[i].islower():
                continue
            elif l[i].isnumeric():
                continue
            else:
                f= 0
                break




    else:
        f=0

    if f==1:print("Success")
    else:print("Error")
                
