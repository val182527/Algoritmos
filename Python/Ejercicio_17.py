"""
Entradas
Presupuesto total-->float-->PT
Salidas
Presupuesto para ginecologia-->float-->PG
Presupuesto para traumatologia-->float-->Pt
Presupuesto para pediatria-->float-->PP
"""
PT=float(input("Ingrese el monto del presupuesto total: "))
PG=(40*PT)/100
Pt=(30*PT)/100
PP=(30*PT)/100
print("presupuesto ginecologia: "+str(PG))
print("presupuesto traumatologia: "+str(Pt))
print("presupuesto pediatria: "+str(PP))

