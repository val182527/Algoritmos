"""
Entradas
capital-->float-->c
porcentaje de interes-->float-->pi
Salidas
dinero generado-->float-->d
"""
c=float(input("Ingrese el capital invertido: "))
pi=float(input("Ingrese el porcentaje de interes: "))
I=(c*pi)/100
if(I>100000):
 print ("Dinero generado por cantidad de intereses: "+str(I))
 print("Reinvertir intereses.")
 d=(c+I)
 print("Total en la cuenta: "+str(d))
else:
 (I<100000)
 print("Dinero generado por cantidad de intereses: "+str(I))
 print("No reinvertir intereses")
