"""
Entradas
Cantidad en metros-->float-->m
Salidas
Pies-->float-->ft
Pulgadas-->float-->In
"""
m=float(input("Ingrese la cantidad en metros: "))
ft=(m/12)
In=(m*39.27)
print("Pies: "+str(ft))
print("Pulgadas: "+str(In))
