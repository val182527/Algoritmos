"""
Entradas
Precio de venta al publico-->float-->PVP
Precio pagado por el producto-->float-->PP
Salidas
Descuento aplicado en porcentaje-->float-->PD
"""
PVP=float(input("Ingrese el precio de venta del producto: "))
PP=float(input("Ingrese el precio pagado por el producto: "))
PD=((PVP-PP)*100)/PVP
print("Porcentaje de descuento: "+str(PD)+"%")
