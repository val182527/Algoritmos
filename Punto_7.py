"""
Entradas
distancia recorrida-->float-->k
Salidas
Precio a pagar-->float-->p
"""
k=float(input("Ingrese la distancia recorrida en km: "))

if(k<=300):
  p=50000
  print("Precio a pagar: "+str(p))
elif(k>300 and k<=1000):
  p=(70000+(k-300)*30000)
  print("Precio a pagar: "+str(p))
elif(k>300 and k>1000):
  p=(150000+(k-300)*9000)
  print("Precio a pagar: "+str(p))
