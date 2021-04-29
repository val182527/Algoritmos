"""
Entradas
Monto de la compra-->float-->m
Nombre del cliente-->str-->n
Salidas
Nombre del cliente-->str-->n
Monto de la compra-->float-->m
Monto a pagar-->float-->mp
Descuento recibido-->float-->d
"""
n=str(input("Ingrese el nombre del cliente: "))
m=float(input("Ingrese el monto de la compra: "))

if(m<=50000):
  d=0
  mp=m
  print((n)+", monto de la compra: $"+str(m)+", monto a pagar: $"+str(mp)+", descuento recibido: $"+str(d))
elif(m>50000 and m<=100000):
  d=(m*0.05)
  mp=(m-d)
  print((n)+", monto de la compra: $"+str(m)+", monto a pagar: $"+str(mp)+", descuento recibido: $"+str(d))
elif(m>100000 and m<=700000):
  d=(m*0.11)
  mp=(m-d)
  print((n)+", monto de la compra: $"+str(m)+", monto a pagar: $"+str(mp)+", descuento recibido: $"+str(d)) 
elif(m>700000 and m<=1500000):
  d=(m*0.18)
  mp=(m-d)  
  print((n)+", monto de la compra: $"+str(m)+", monto a pagar: $"+str(mp)+", descuento recibido: $"+str(d)) 
elif(m>1500000):
  d=(m*0.25)
  mp=(m-d)  
  print((n)+", monto de la compra: $"+str(m)+", monto a pagar: $"+str(mp)+", descuento recibido: $"+str(d))
   


