d = {"Icosahedron":20 ,
     "Cube":6 ,
     "Tetrahedron":4 ,
     "Dodecahedron":12 ,
     "Octahedron":8 }
s=0
for i in range(int(input())):
    s+=d[input()]
print(s)