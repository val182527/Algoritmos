#3.	Desarrolle un algoritmo o programa que permita calcular y mostrar la suma  de todos los números pares comprendidos entre 97 y 1003. Respuesta: 249150 
"""
Entradas
numeros pares-->int-->numeros pares
Salidas
suma-->int-->contador
"""

contador=0
for i in range(97,1004):
 if(i%2==0):
   contador=contador+i
print(contador)
