"""
Entradas
Lectura de la factura-->float-->L
Costo kilovatio-->float-->CK
Salidas
Monto total de la factura-->float-->MT
"""
L=float(input("Ingrese la lectura de su factura: "))
CK=float(input("ingrese el costo del kilovatio: "))
MT=(L*CK)
print("Monto total de su factura: "+str(MT))