"""
Entradas
Cantidad de galones-->float-->gal
Salidas
Precio final por litro-->float-->COP
"""
gal=float(input("Ingrese la cantidad en galones: "))
COP=(gal*3.785)*(50000)
print("Precio total: $"+str(COP))
