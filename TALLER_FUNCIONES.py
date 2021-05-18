frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')

lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt
lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt
"""
Entradas
Lista de frutas txt-->list-->frutas
Lista de mumeros txt-->list-->numeros
Salidas
lista de frutas-->list-->lista_frutas
lista de numeros-->list-->lista_numeros
"""
for i in frutas:
  lista_frutas.append(i)

for i in numeros:
  lista_numeros.append(i)

print("LISTA DE FRUTAS")
print(lista_frutas)
print("")
print("LISTA DE NUMEROSS")
print(lista_numeros)


#Realizar una funcion que elimine un caracter de todos los elementos de la lista
"""
Entradas
lista-->list-->lista
elemento-->str-->e
Salidas
lista-->lista
"""

def eliminar_caracter(lista, e):
 lista_auxiliar=[]
 for i in lista:
   c=i.replace(e,"")
   lista_auxiliar.append(c)
 return lista_auxiliar


#Realizar una funcion que retorne la copia de una lista que pasa por parametro 
"""
Entradas
lista-->list-->lista
Salidas
copia de la lista-->str-->lista.copy
"""
def copia_lista(lista):
  return lista.copy() 

#Realizar una funcion que retorne una lista de numeros enteros   
"""
Entradas
lista-->list-->lista
Salidas
lista numeros enteros-->int-->lista_enteros
"""
def numeros_pares(lista):
  auxiliar=[]
  for i in lista:
    if(float(i)%2==0):
      auxiliar.append(i)
  return auxiliar
    

#Realizar una funcion que elimine un elemento de una lista
"""
Entradas
lista-->list-->lista
elemento-->str-->e
Salidas
lista nueva-->str-->lista_nueva
"""

def eliminar_elemento(lista, e):
  lista.remove(e)
  return lista

#Realizar una funcion que retorne el tamaño de una lista  
"""
Entradas
lista-->list-->lista
Salidas
tamaño de lista-->int-->t
"""
t=lista_numeros
print("")
print("TAMAÑO DE LISTA")
print(len(t))

#Retorna el tamaño de la lista y que tipo de datos estan dentro de la lista
"""
Entradas
lista-->list-->lista
Salidas
tamaño de lista-->int-->t
tipo de datos-->str-->tipo
"""
t=lista_frutas
print("")
print("TAMAÑO DE LISTA Y TIPO DE DATOS")
print(len(t))
tipo=(type(lista_frutas))
print(tipo)

#Retornar una lista con los numero negativos  
"""
Entradas
lista-->list-->lista
Salidas
lista numeros negativos-->float-->LN
"""  
def numeros_negativos(lista):
  auxiliar=[]
  for i in lista:
    if(lista<0):
      auxiliar.append(i)
  return auxiliar


#realizar una funcion que retorne la posicion de un elemento que pasa por parametro
"""
Entradas
lista-->list-->lista
Salidas
Posicion-->int-->p
"""

l=lista_numeros
p=(l.index('33\n'))
print("")
print("POSICION")
print(p)

#realizar una funcion que agregue al final de archivo frutas una fruta
"""
Entradas
lista frutas-->list-->lista_frutas
Salidas
Lista nueva-->str-->ListaNueva
"""
l=lista_frutas
p=(l.insert(44, "sandia"))
ListaNueva=(l[43])
print("")
print("INSERTAR FRUTA AL FINAL DE LA LISTA")
print(lista_frutas)


#Realizar una funcion que cuente el numero de veces que se repite un elemento  
"""
Entradas
lista-->list-->lista
Salidas
repeticiones-->int-->r
"""

l=lista_numeros
r=(l.count('123\n'))
print("")
print("REPETICION DE ELEMENTO")
print(r)


if __name__ == "__main__":

  nl=eliminar_caracter(lista_frutas, "P")
  print("")
  print("LISTA DE FRUTAS ORIGINAL")
  print(lista_frutas)
  print("")
  print("LISTA DE FRUTAS NUEVA CON CARACTER ELIMINADO")
  print(nl)
  
  nueva=eliminar_caracter(lista_numeros, "\n")
  nl=numeros_pares(nueva)
  print("")
  print("ELEMENTO ELIMINADO")
  print(eliminar_elemento(nl, "32"))

  n=eliminar_caracter(lista_frutas, "\n")
  print("")
  print("ELIMINAR SALTO DE ESPACIO")
  print(n)
  tipo=eliminar_caracter(lista_frutas,"\n")
  print("ELIMINAR CARACTER")
  print(tipo)

