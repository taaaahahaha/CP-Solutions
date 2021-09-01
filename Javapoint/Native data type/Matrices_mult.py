m1 = [[1,2,3],
      [4,5,6],
      [7,8,9]]
m2 = [[10,11,12],
      [13,14,15],
      [16,17,18]]
ans = [[0,0,0],
       [0,0,0],
       [0,0,0]]

for i in range(3): #rows 0
      for j in range(3): #column 1
            for k in range(3):
                  ans[i][j] += m1[i][k] * m2[k][j]
for a in ans:
      print(a)