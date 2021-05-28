
preferencia = 0
alcohol = 0
gasolina = 0
diesel = 0

while preferencia != 4:
    preferencia = int(input())
    
    if(preferencia == 1):
        alcohol += 1
    
    if(preferencia == 2):
        gasolina += 1
    
    if(preferencia == 3):
        diesel += 1

print("MUITO OBRIGADO")
print("Alcool: %d" %alcohol)
print("Gasolina: %d" %gasolina)
print("Diesel: %d" %diesel)