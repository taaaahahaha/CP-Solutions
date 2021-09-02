n = int(input())
five = n%5==0
eleven = n%11==0

if five or eleven:
    if five and eleven:
        print("BOTH")
    else:
        print("ONE")
else:
    print('NONE')
       