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
copia de la lista-->str-->copia 
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
def numeros_enteros(lista):
  auxiliar=[]
  original=[]
  for i in lista:
    auxiliar.append(float(i))
  for n in auxiliar:
    original.append(int(n))
  return original
    
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

#Retorna una lista con las palabras iniciales con la letra que pasa por parametro  
"""
Entradas:
lista-->list-->lista
Salidas
lista-->list-->palabras
"""  
def letra_inicial(lista):
  for word in lista_frutas:
    if word.startswith("A"):
      print(word)

#Realizar una funcion que retorne el tamaño de una lista  
"""
Entradas
lista-->list-->lista
Salidas
tamaño de lista-->int-->t
"""
def tamano_lista(lista):
  return len(lista_numeros)

#Retorna el tamaño de la lista y que tipo de datos estan dentro de la lista
"""
Entradas
lista-->list-->lista
Salidas
tamaño de lista-->int-->t
tipo de datos-->str-->tt
"""
def tipo_lista(lista):
  for i in range(len(lista_frutas)):
    return len(lista_frutas), type(lista_frutas[i])

#Retornar una lista con los numeros negativos  
"""
Entradas
lista-->list-->lista
Salidas
lista numeros negativos-->float-->numerosn
"""  
def numeros_negativos(lista):
  auxiliar=[]
  for i in lista:
    if(float(i)<=0):
      auxiliar.append(i)
  return auxiliar
 
#realizar una funcion que retorne la posicion de un elemento que pasa por parametro
"""
Entradas
lista-->list-->lista
Salidas
Posicion-->int-->p
"""
def posicion(lista):
  return (lista_frutas.index('Kiwi\n'))

#realizar una funcion que agregue al final de archivo frutas una fruta
"""
Entradas
lista frutas-->list-->lista_frutas
Salidas
Lista nueva-->str-->ListaNueva
"""
def agregar_fruta(lista):
  lista_frutas.append("Mangostino")

#Realizar una funcion que cuente el numero de veces que se repite un elemento  
"""
Entradas
lista-->list-->lista
Salidas
repeticiones-->int-->repeticion
"""
def repetir_elemento(lista):
  return (lista_numeros.count('123\n'))

if __name__ == "__main__":
  print("LISTA DE FRUTAS")
  print(lista_frutas)
  print("LISTA DE NUMEROS")
  print(lista_numeros)

  nl=eliminar_caracter(lista_frutas, "P")
  print("LISTA DE FRUTAS CON CARACTER ELIMINADO")
  print(nl)

  numeroE=numeros_enteros(lista_numeros)
  print("NUMEROS ENTEROS")
  print(numeroE)

  e=eliminar_elemento(lista_numeros, "123\n")
  print("ELEMENTO ELIMINADO")
  print(e)

  print("PALABRAS QUE INICIAN POR UNA LETRA")
  palabras=letra_inicial(lista_frutas)
  print(palabras)
  
  t=tamano_lista(lista_numeros)
  print("TAMAÑO DE LISTA")
  print(t)

  tt=tipo_lista(lista_frutas)
  print("TAMAÑO Y TIPO DE LISTA")
  print(tt)

  numerosn=numeros_negativos(lista_numeros)
  print("NUMEROS NEGATIVOS")
  print(numerosn)

  p=posicion(lista_frutas)
  print("POSICION")
  print(p)
   
  agregar_fruta(lista_frutas)
  print("ELEMENTO AL FINAL DE LA LISTA")
  print(lista_frutas)

  repeticion=repetir_elemento(lista_numeros)
  print("REPETICION DE ELEMENTO")
  print(repeticion)










