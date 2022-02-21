for _ in range(int(input())):
    n = input()
    last = n[-1]
    if last == '0':
        print('0') 
    elif last == '5':
        print('1')
    else:
        print('-1')

