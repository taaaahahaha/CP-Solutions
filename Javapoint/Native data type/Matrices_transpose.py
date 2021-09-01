m = [[1,2],
     [3,4],
     [5,6]]

a = [[0,0,0],
     [0,0,0]]
    
for j in range(len(m[0])):
    for i in range(len(m)):
        a[j][i] = m[i][j]

for ans in a:
    print(ans)