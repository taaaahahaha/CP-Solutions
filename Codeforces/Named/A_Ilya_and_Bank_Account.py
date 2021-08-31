n = input()
t1 = n[:-1]
t2 = n[:-2]+n[-1]

print(max(int(n),int(t1),int(t2)))