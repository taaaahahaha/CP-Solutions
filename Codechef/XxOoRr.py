import math

def binary(n):
    return bin(n).replace("0b", "")

for _ in range(int(input())):
    c=0
    n,k=map(int,input().strip().split())
    a = [int(i) for i in input().split()]
    a.sort()
    bin_list = [int(binary(i)) for i in a]
    p=0
    while(bin_list[len(bin_list)-1] != 0):
        temp=0
        for i in range(len(bin_list)):
            if bin_list[i]%10!=0 : temp+=1
            bin_list[i] //= 10
        c += math.ceil(temp/k)
    print(c)