n,m = map(int,input().split())

for i in range(1,n+1):
    if i%2==0:
        if i%4==0:
            print('#'.ljust(m,'.'))
        else:
            print('#'.rjust(m,'.'))
    else:
        print('#'*m)

