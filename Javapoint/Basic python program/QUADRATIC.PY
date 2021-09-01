a,b,c=(float(i) for i in input().split())
if(b**2-4*a*c<0):print("Imaginary solutions")
else:print((-b + (b**2 -4*a*c)**0.5)//(2*a),(-b - (b**2 -4*a*c)**0.5)//(2*a))