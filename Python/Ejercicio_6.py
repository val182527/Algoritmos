"""
Entradas
Número de mujeres-->int-->M
Numero de hombres-->int-->H
Salidas
Porcentaje de mujeres-->float-->PM
Porcentaje de hombres-->float-->PH
"""
M=int(input("Ingrese el número de mujeres: "))
H=int(input("Ingrese el número de hombres: "))
PM=(M*100)/(M+H)
PH=(H*100)/(M+H)
print("Porcentaje de mujeres: "+str(PM))
print("Porcentaje de hombres: "+str(PH))
