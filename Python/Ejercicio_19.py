"""
Entrada
Naranjas compradas-->int-->X
Valor de naranja por docena-->float-->Y
Venta de naranjas-->float-->K
Salidas
Total de la inversion-->float-->TI
Ganancia real-->float-->GR
Porcentaje de ganancia-->float-->PG
"""
X=int(input("Ingrese el numero de naranjas compradas: "))
Y=float(input("Ingrese el valor de la docena: "))
K=float(input("Ingrese la venta de naranjas: "))
TI=(X/12)*(Y)
GR=(K-TI)
PG=(GR*100)/TI
print("Porcentaje de ganancia total: "+str(PG),"%")
