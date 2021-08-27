a,b,m1,m2=0,0,0,0
lead=0
player_won = []
lead = []
for _ in range(int(input())):
    x,y = map(int,input().strip().split())
    a+=x
    b+=y
    if a>b:
        diff = a-b
        player_won.append(1)
        lead.append(diff)
    else:
        diff = b-a
        player_won.append(2)
        lead.append(diff)
# print(player_won)
# print(lead)
ind_max = lead.index(max(lead))
print(player_won[ind_max],max(lead))