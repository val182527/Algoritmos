"""
Entradas
Precio por hora-->float-->PH
Descuento por impuestos-->float-->I
Salidas
Salario base-->float-->SB
Porcentaje de descuento por impuesto-->float-->DI
Salario neto-->float-->SN
"""
HT=float(input("Ingrese las horas trabajadas: "))
PH=float(input("Ingrese el precio por hora: "))
I=float(input("Ingrese el descuento por impuestos: "))

SB=HT*PH
DI=(SB*I)/100
SN=(SB-DI)
print("Salario neto: "+str(SN))
