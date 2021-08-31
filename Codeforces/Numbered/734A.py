i = input
n = int(i())
w = i()

nA = w.count("A")
nB = w.count("D")

if(nA>nB) : print("Anton")
elif(nB>nA) : print("Danik")
else : print("Friendship")
