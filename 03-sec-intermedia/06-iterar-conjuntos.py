#iterando conjuntos con for


animales = {"perro","gato", "loro", "cocodrilo"}
for animal in animales:
    print(f'ahora la variable animales es : {animal}')

#recorriendo conjuntos y multiplicando cada uno por 10
numeros = {10, 62, 123, 70}
for multiplicador in numeros:
    resultado = multiplicador*2
    print(resultado)

#iterando dos o mas conjuntos del mismo tamano al mismo tiempo
for multiplicador, animal in zip(animales,numeros):
    print(f'recorriendo  conjunto 1: {multiplicador}')
    print(f'recorriendo conjunto 2: {animal}')


#forma correcta de recorrer una conjunto con su indice 
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')

#usando el else
for numero in  numeros:
    print(f'ejecutando el ultimo bucle, valor actual: {numero}')
else:
    print("el bucle termino")

#tod lo anterior funciona exactamente igual para tuplas y conjuntos wey