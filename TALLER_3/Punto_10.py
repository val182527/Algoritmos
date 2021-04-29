"""
Entradas
Categoría-->int-->c
Salario bruto-->float-->sb
Salidas
Aumento-->float-->a
"""
c=int(input("Ingrese la categoría: "))
sb=float(input("Ingrese el salario bruto: "))

if(c==1):
  a=(sb+(sb*0.1))
  print("Salario neto: "+str(a))
elif(c==2):
  a=(sb+(sb*0.15))
  print("Salario neto: "+str(a))
elif(c==3):
  a=(sb+(sb*0.20))
  print("Salario neto: "+str(a))
elif(c==4):
  a=(sb+(sb*0.40))
  print("Salario neto: "+str(a)) 
elif(c==5):
  a=(sb+(sb*0.60))
  print("Salario neto: "+str(a)) 
  