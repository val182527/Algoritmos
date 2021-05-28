#6.	Efectuar la división de dos números enteros, utilizando el método de las restas sucesivas. Observe el siguiente ejemplo:

"""
Entradas
numero1-->int-->n1
numero2-->int-->n2
Salidas 
resultado-->float-->cont
"""
cont=int(0)

n1=int(input("Ingrese el dividendo: "))
n2=int(input("Ingrese el divisor: "))

n1=n1-n2

while(n1>=0):
  cont=cont+1
  n1=n1-n2
print(cont)

