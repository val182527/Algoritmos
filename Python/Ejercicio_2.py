"""
Entradas
Dinero invertido-->int-->D
Salidas
Total de dinero al mes-->float-->TD
"""
D=int(input("Ingresar la suma de dinero invertida: "))
P=(2*D)/100
TD=(D+P)
print("Total al mes: "+str(TD))
