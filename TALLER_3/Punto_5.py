"""
Entradas
Importe global departamento A-->float-->a
Importe global departamento B-->float-->b
Importe global departamento C-->float-->c
Salario-->float-->s
Salidas
Salario neto-->float-->sn
"""
a=float(input("Ingrese el importe del departamento A: "))
b=float(input("Ingrese el importe del departamento B: "))
c=float(input("Ingrese el importe del departamento C: "))
s=float(input("Ingrese el salario del trabajador: "))

vt=(a+b+c)
p=(vt*0.33)
if(a>p):
  sn=s+(s*0.20)
  print("Salario neto + incremnto vendedores departamento A: $"+str(sn))
else:
  (a<p)
  print("Salario neto sin incremento vendedores departamento A: $"+str(s))
if(b>p):
  sn=s+(s*0.20)
  print("Salario neto + incremento vendedores departamento B: $"+str(sn))
else:
  (b<p)
  print("Salario neto sin incremento vendedores departamento B: $"+str(s))

if(c>p):
  sn=s+(s*0.20)
  print("Salario neto + incremento vendedores departamento C: $"+str(sn))
else:
  (c<p)
  print("Salario neto sin incremento vendedores departamento C: $"+str(s))
