"""
Entradas
-Matemáticas
Calificación exámen final-->int-->EFM
Tarea 1 matemáticas-->int-->T1M
Tarea 2 matemáticas-->int-->T2M
Tarea 3 matemáticas-->int-->T3M
-Física
Calificación exámen final-->int-->EFF
Tarea 1 física-->int-->T1F
Tarea 2 física-->int-->T2F
-Química
Calificación exámen final-->int-->EFQ
Tarea 1 química-->int-->T1Q
Tarea 2 química-->int-->T2Q
Tarea 3 química-->int-->T3Q

Salidas
-Matemáticas
Porcentaje exámen final matemáticas-->float-->PEFM
Promedio tareas matemáticas-->float-->PTM
Porcentaje tareas matemáticas-->float-->PPTM
Calificación final de matemáticas-->float-->CFM
-Física
Porcentaje exámen final física-->float-->PEFF
Promedio tareas física-->float-->PTF
Porcentaje tareas física-->float-->PPTF
Calificación final de física-->float-->CFF
-Química
Porcentaje exámen final química-->float-->PEFQ
Promedio tareas química-->float-->PTQ
Porcentaje tareas química-->float-->PPTQ
Calificación final de química-->float-->CFQ

Promedio general de las tres materias-->float-->PG
"""
"""
Entradas
Matemáticas
"""
input("Matemáticas")
EFM=int(input("Ingrese calificación exámen final: "))
T1M=int(input("Ingrese la calificación de la tarea 1: "))
T2M=int(input("Ingrese la calificación de la tarea 2: "))
T3M=int(input("Ingrese la calificación de la tarea 3: "))
"""
Física
"""
input("Física")
EFF=int(input("Ingrese calificación exámen final: "))
T1F=int(input("Ingrese la calificación de la tarea 1: "))
T2F=int(input("Ingrese la calificación de la tarea 2: "))
"""
Química
"""
input("Química")
EFQ=int(input("Ingrese calificación exámen final: "))
T1Q=int(input("Ingrese la calificación de la tarea 1: "))
T2Q=int(input("Ingrese la calificación de la tarea 2: "))
T3Q=int(input("Ingrese la calificación de la tarea 3: "))
"""
Salidas
"""
PEFM=(EFM*90)/100
PTM=(T1M+T2M+T3M)/3
PPTM=(PTM*10)/100
CFM=(PEFM+PPTM)

PEFF=(EFF*80)/100
PTF=(T1F+T2F)/2
PPTF=(PTF*20)/100
CFF=(PEFF+PPTF)

PEFQ=(EFQ*85)/100
PTQ=(T1Q+T2Q+T3Q)/3
PPTQ=(PTQ*15)/100
CFQ=(PEFQ+PPTQ)

PG=(CFM+CFF+CFQ)/3

print("Promedio general de las tres materias: "+str(PG))
print("Promedio matemáticas: "+str(CFM))
print("Promedio Física: "+str(CFF))
print("Promedio química: "+str(CFQ))
