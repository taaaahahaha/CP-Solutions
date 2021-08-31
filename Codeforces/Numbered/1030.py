n = int(input())
li = [int(i) for i in input().split()]
c=0
for _ in li:
    if _ == 1: c=1
if c==1 : print("HARD")
else: print("EASY")