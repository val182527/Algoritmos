"""
Entradas
Parcial1-->float-->P1
Parcial2-->float-->P2
Parcial3-->float-->P3
Examen final-->float-->EF
Trabajo final-->float-->TF
Salidas
Calificación de parciales-->float-->CParciales
Calificación del examen final-->float-->CExamenF
Calificación del trabajo final-->float-->CTrabajoF
Calificación final de la materia -->float-->CF
"""
P1=float(input("Ingrese nota del parcial 1: "))
P2=float(input("Ingrese nota del parcial 2: "))
P3=float(input("Ingrese nota del parcial 3: "))
EF=float(input("Ingrese nota del examen final: "))
TF=float(input("Ingrese nota del trabajo final: "))
CParciales=(((P1+P2+P3)/3)*(55))/100
CExamenF=(30*EF)/100
CTrabajoF=(15*TF)/100
CF=(CParciales+CExamenF+CTrabajoF)
print("Calificacón final materia de computación: "+str(CF))
