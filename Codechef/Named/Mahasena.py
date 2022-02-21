ii = lambda: int(input())
imi = lambda: [int(i) for i in input().split()]

n = ii()
li = imi()
e=o=0
for i in li:
    if i%2==0:e+=1
    else:o+=1

if e>o:print("READY FOR BATTLE")
else:print("NOT READY")