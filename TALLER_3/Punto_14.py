"""
Entradas
Lectura anterior-->float-->L1
Lectura actual-->float-->L2
Salidas
Monto a pagar-->float-->M
"""
L1=float(input("Ingrese la lectura anterio: "))
L2=float(input("Ingrese la lectura actual: "))

L=(L1-L2)

if(L>0 and L<=100):
  M=L*4600
  print("Monto a pagar: $"+str(M))
elif(L>101 and L<=300):
 M=L*80000
 print("Monto a pagar: $"+str(M))
elif(L>301 and L<=500):
 M=L*100000
 print("Monto a pagar: $"+str(M))
elif(L>501):
 M=L*120000
 print("Monto a pagar: $"+str(M))
