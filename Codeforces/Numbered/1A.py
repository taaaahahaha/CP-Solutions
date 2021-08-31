import math
n,m,a = map(int,input().strip().split())
print(math.ceil(m/a)*math.ceil(n/a))