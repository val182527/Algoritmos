#2.	Escriba un programa que imprima todos los enteros positivos impares menores que 100 omitiéndose aquellos que sean divisibles por 7.
"""
Entradas
numeros de 1 a 101-->int-->numeros
Salidas
enteros positivos-->int-->i
"""

for i in range (1,101):
  if(i%7==0):
    continue
  print(i)
