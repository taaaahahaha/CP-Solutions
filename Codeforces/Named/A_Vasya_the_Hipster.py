a,b = map(int,input().split())

min_socks = min(a,b)
max_socks = max(a,b)

print(min_socks,(max_socks-min_socks)//2)