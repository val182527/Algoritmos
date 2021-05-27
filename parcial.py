T = int(input())
lista = []
for i in range (T):
  c = str(input())
  lista.append(c)

for x in range(0,len(lista)):
   if lista[x] == "papel tijera" :
    print ("Caso #", x+1,": ¡Siempre hay un proximo semestre!")
   elif lista[x] == "papel piedra" :
    print ("Caso #", x+1,": ¡LaVidaEsDura!")
   elif lista[x] == "papel lagarto" :
    print ("Caso #", x+1,": ¡Siempre hay un proximo semestre!")
   elif lista[x] == "papel Holk" :
    print ("Caso #", x+1,": ¡LaVidaEsDura!")
   elif lista[x] == "papel papel" :
    print ("Caso #", x+1,": ¡Otra vez!")
   elif lista[x] == "tijera papel" :
    print ("Caso #", x+1,": ¡LaVidaEsDura!")
   elif lista[x] == "tijera piedra" :
    print ("Caso #", x+1,": ¡Siempre hay un proximo semestre!")
   elif lista[x] == "tijera lagarto" :
    print ("Caso #", x+1,": ¡LaVidaEsDura!")
   elif lista[x] == "tijera Holk" :
    print ("Caso #", x+1,": ¡Siempre hay un proximo semestre!")
   elif lista[x] == "tijera tijera" :
    print ("Caso #", x+1,": ¡Otra vez!")
   elif lista[x] == "piedra papel" :
    print ("Caso #", x+1,": ¡Siempre hay un proximo semestre!")
   elif lista[x] == "piedra tijera" :
    print ("Caso #", x+1,": ¡LaVidaEsDura!")
   elif lista[x] == "piedra lagarto" :
    print ("Caso #", x+1,": ¡LaVidaEsDura!")
   elif lista[x] == "piedra Holk" :
    print ("Caso #", x+1,": ¡Siempre hay un proximo semestre!")
   elif lista[x] == "piedra piedra" :
    print ("Caso #", x+1,": ¡Otra vez!")
   elif lista[x] == "lagarto papel" :
    print ("Caso #", x+1,": ¡LaVidaEsDura!")
   elif lista[x] == "lagarto tijera" :
    print ("Caso #", x+1,": ¡Siempre hay un proximo semestre!")
   elif lista[x] == "lagarto piedra" :
    print ("Caso #", x+1,": ¡Siempre hay un proximo semestre!")
   elif lista[x] == "lagarto Holk" :
    print ("Caso #", x+1,": ¡LaVidaEsDura!")
   elif lista[x] == "lagarto lagarto" :
    print ("Caso #", x+1,": ¡Otra vez!")
   elif lista[x] == "Holk papel" :
    print ("Caso #", x+1,": ¡Siempre hay un proximo semestre!")
   elif lista[x] == "Holk tijera" :
    print ("Caso #", x+1,": ¡LaVidaEsDura!")
   elif lista[x] == "Holk piedra" :
    print ("Caso #", x+1,": ¡LaVidaEsDura!")
   elif lista[x] == "Holk lagarto" :
    print ("Caso #", x+1,": ¡Siempre hay un proximo semestre!")
   elif lista[x] == "Holk Holk" :
    print ("Caso #", x+1,": ¡Otra vez!")