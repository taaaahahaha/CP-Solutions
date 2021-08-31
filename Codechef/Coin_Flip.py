# Taaha Multani @ https://github.com/taaaahahaha

def iil():
    return [int(i) for i in input().split()]
def imi():
    return map(int,input().strip().split())
def ii():
    return int(input())



for _ in range(ii()):
    for __ in range(ii()):
        i,n,q = imi()
        # if i==1:
        #     coins = ["H"]*n
        # else:
        #     coins = ["T"]*n
        # if n%2!=0:
        #     for i in range(0,n+1,2):
        #         if coins[i] == "H":
        #             coins[i] = "T"
        #         else:
        #             coins[i] = "H"
        # else:
        #     for i in range(1,n+1,2):
        #         if coins[i] == "H":
        #             coins[i] = "T"
        #         else:
        #             coins[i] = "H"
        # if q == 1:
        #     print(coins.count("H"))
        # else:
        #     print(coins.count("T"))

        if n%2==0:
            print(n//2)
        else:
            if q==i:
                print(n//2)
            else:
                print(n-n//2)
# HHHHH
# THHHH
# HTHHH
# THTHH
# HTHTH
# THTHT

# HHHH
# THHH
# HTHH
# THTH
# HTHT








