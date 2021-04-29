"""
Entradas
A-->int-->A
B-->int-->B
C-->int-->C
D-->int-->D
Salidas
Resultado-->float-->R
"""
A=int(input("Ingrese un número entero positivo: "))
B=int(input("Ingrese un número entero positivo: "))
C=int(input("Ingrese un número entero positivo: "))
D=int(input("Ingrese un número entero positivo: "))
if(D==0):
 R=(A-C)**2
 print("El resultado es: "+str(R))
if(D>0):
  R=((A-B)**3)/D
  print("El resultado es: "+str(R))
