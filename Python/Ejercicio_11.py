"""
Entradas
Nombre del trabajador-->str-->Nombre
Número de horas trabajadas-->float-->HT
Precio por hora de trabajo-->float-->PHT
Número de horas extras trabajadas-->float-->HET
Porcentaje de pago por horas extras trabajadas-->float-->PorcentajeHE

Deducciones
Porcentaje por paro forzo-->float-->PF
Porcentaje de política habitacional-->float-->PolH
Porcentaje por caja de ahorro-->float-->PCA

Asignaciones
Actualización academica-->float-->AA
Asignación por cada hijo-->float-->AH
Asignación de prima por hogar-->float-->AP

Salidas
Sueldo normal-->float-->S
Incremento por hora extra-->float-->IHE
Pago por hora extra-->float-->PHE
Sueldo base-->float-->SB

Deducciones-->float-->D
Asignaciones-->float-->A
Sueldo neto del mes de Diciembre-->float-->SN
"""
Nombre=str(input("Ingrese su nombre: "))
HT=float(input("Ingrese las horas trabajadas: "))
PHT=float(input("Ingrese el precio por hora trabajada: "))
HET=float(input("Ingrese las horas extra trabajadas: "))
PorcentajeHE=float(input("Ingrese el porcentaje de pago por hora extra trabajada: "))

PF=float(input("Ingrese el porcentaje por paro forzoso: "))
PolH=float(input("Ingrese el porcentaje de política habitacional"))
PCA=float(input("Ingrese el porcentaje por caja de ahorro: "))

AA=float(input("Ingrese la asignación por actualización académica: "))
AH=float(input("Ingrese la asignación por cada hijo: "))
AP=float(input("Ingrese la asignación de prima por hogar : "))

S=(HT*PHT)
IHE=(PHT*PorcentajeHE)/100
PHE=(HET*PHT)+(IHE)
SB=(S+PHE)

D=((PF+PolH+PCA)*SB)/100
A=(AA+AH+AP)

SN=(SB+A)-D
print("Total de asignaciones: "+str(A))
print("Total de deducciones: "+str(D))
print(Nombre,(", su sueldo neto para el mes de Diciembre es: "+str(SN)))
