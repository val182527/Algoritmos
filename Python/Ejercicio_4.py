"""
Entradas
Total de la compra-->float-->T
Salidas
Total de la compra -15%-->float-->D
"""
T=float(input("Ingrese el total de la compra: "))
P=(15*T)/100
D=(T-P)
print("El total de su compra es: "+str(D))
