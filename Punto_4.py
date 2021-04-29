"""
Entradas
monto de la compra-->float-->m
Salidas
Inversión de los fondos de la empresa-->float-->f
Cantidad a pagar a crédito-->float-->c
Monto por intereses-->float-->i
Cantidad prestada del banco-->float-->b
"""
m=(float(input("Ingrese el monto total de la compra: ")))
if(m>5000000):
  f=(m*0.55)
  b=(m*0.30)
  csi=(m*0.15)
  i=(csi*0.20)
  c=(csi+i)
  print("Inversión por fondos de la empresa: $"+str(f))
  print("Cantidad a pagar a crédito: $"+str(c))
  print("Monto por intereses: $"+str(i))
  print("Cantidad prestada del banco: $"+str(b))

else:
  (m<5000000)
  f=(m*0.70)
  csi=(m*0.30)
  i=(csi*0.20)
  c=(csi+i)
  print("Inversión por fondos de la empresa: $"+str(f))
  print("Cantidad a pagar a crédito: $"+str(c))
  print("Monto por intereses: $"+str(i))

