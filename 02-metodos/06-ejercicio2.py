#EJERCICO 2
# A) pedirle al usuario que diga cualquier texto real y:
#- Calcular cuanto tardaria en decir esa frase
#Cuantas paabras dijo

# b) si se tarda mas de un minuto :

# - decile "para flaco tampoc te pedi un tertamento"

# C) Dalto habla un 30% mas rapido Cuanto tardaria dalto el en decirlo?

frase = input("decime una frasae y te calculo cuanto tardarias si tuvieras que decirla. :")
palabra_separadas = frase.split(" ")
cantidad_de_palabras = len(palabra_separadas)

print(f'digiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo')
print(f'Dalto lo haria {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2*1.3} segundos en decirlo')
if(cantidad_de_palabras > 12) :
    print("pra flaco tampoco te pedi un testamento")