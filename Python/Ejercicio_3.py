"""
Entrandas
venta1->float->v1
Venta2->float->v2
venta3->float->v3
sueldobase->float->sb
Salidas
comision->float->c
tota->flotar->total
"""
v1=float(input("Digite la venta1: "))
v2=float(input("Digite la venta2: "))
v3=float(input("Digite la venta3: "))
sb=float(input("Digite Suedo base: "))
c=((v1+v2+v3)/3)*0,10
total=sb+c
print("la comision es:"+str(c),"sueldo total:"+str( total ))