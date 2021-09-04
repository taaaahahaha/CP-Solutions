y,w=map(int,input().split())
max_num = max(y,w)
choices = 6-(max_num-1)
total = 6

def hcf(a,b):
    if (b == 0):
         return a
    return hcf(b, a%b)
 
cf = (hcf(total,choices))

print(f"{choices//cf}/{total//cf}")
