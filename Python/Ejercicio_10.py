"""
Entradas
Chelines Austriacos-->float-->Chelines
Dracmas griegos-->float-->Dracmas
Pesetas-->float-->Pesetas
Chelines a pesetas-->float-->CaP
Salidas
Chelines a pesetas-->float-->CaP
Dracmas griegos a francos franceses-->float-->DaF
Pesetas a dolares-->float-->PaD
Pesetas a liras italianas-->float-->PaL
"""
Chelines=float(input("Ingrese el valor en chelines: "))
Dracmas=float(input("ingrese el valor en dracmas: "))
Pesetas=float(input("Ingrese el valor en pesetas: "))
CaP=(Chelines*956.87)/100
DaF=(((Dracmas*88.607)/100)/20.110)
PaD=(Pesetas/122.49)
PaL=(Pesetas*100)/9.289
print("Equivalente en pesetas: "+str(CaP))
print("Equivalente en francos: "+str(DaF))
print("Equivalente en dolares: "+str(PaD))
print("Equivalente en liras: "+str(PaL))


