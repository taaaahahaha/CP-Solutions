for i in range(int(input())):
    s = input()
    l = list(s)
    c=0  #</h1>
    for i in range(2,len(l)-1):
        if l[i].isnumeric():continue
        elif not l[i].isalpha() or l[i].isupper() or len(s.strip())==0:c=1
    if s[:2]=="</" and s[len(l)-1]=='>' and c==0:
        print("Success")
    else:
        print("Error")
    