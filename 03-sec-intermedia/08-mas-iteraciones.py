frutas = ["manzana","platano", "Ciruela", "pera", "granada", "naranja", "durazno"]
cadena = "hola limber"
numeros = [2, 5, 6, 12, 100]


for fruta in frutas:
    if fruta == 'granada':
        continue
    print(f'me voy a comer una {fruta}')

print("____________ bucle terminado")

#recorrer una cadena de texto

for letra in cadena:
    print(letra)

#for en una sola linea de codigo (duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)