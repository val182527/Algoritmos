#1.	Sea N y K dos enteros positivos, con K < N. Se desea escribir un programa que escriba el valor de N,N­1,N­2,..., y así sucesivamente hasta llegar al valor de K.
"""
Entradas
N-->int-->N
K-->int-->K
Salidas
valor-->int-->K
"""
N=int(input("Ingrese N: "))
K=int(input("Ingrese K: "))


cond=N+1
while(N>K):
  lista=[]
  for i in range(K,cond):
    lista.append(i)
  lista.sort(reverse=True)
  print(lista)
  break
else:
  print("Error: Ingrese un número (K) menor que N")


