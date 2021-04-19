"""
Entradas
Lado a-->float-->a
Lado b-->float-->b
Lado c-->float-->c
Salidas
Semiperímetro-->float-->S
Área del triángulo-->float-->A
"""
a=float(input("Ingrese el lado a del triángulo: "))
b=float(input("Ingrese el lado b del triángulo: "))
c=float(input("Ingrese el lado c del triángulo: "))
S=(a+b+c)/2
A=(S*(S-a)*(S-b)*(S-c))**1/2
print("Área del triángulo: "+str(A))
