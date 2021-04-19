"""
Entradas
Capital-->float-->C
Tiempo-->float-->T
Tasa--->int-->TS

Salidas
Intereses-->float-->I
Porcentaje del prestamo--float-->PP
Interes anual-->float-->IA
"""
C=float(input("Ingrese el capital: "))
T=float(input("Ingrese el plazo de cobro: "))
TS=int(input("Ingrese la tasa de interes: "))

I=(C*T*TS)/100
PP=(I*100)/C
IA=(PP/4)
print("El pocentaje anual cobrado fue: "+str(IA))
