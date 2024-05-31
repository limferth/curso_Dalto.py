

numeros = [4,7,1,12,45]

#encontrando el numero mayor de una lista
numeros_mas_altos = max(numeros)
print(numeros_mas_altos)
#encontrando el numero menor de una lista

numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

#redondeando a 6 decimales
numero = round(12.4521256,2)
print(numero)

# BOOL = Retorna false -> 0, false, None / o retorna true -> distindo de 0, True, cadena, datos no vacios

resultado_bool = bool("dfhd")
print(resultado_bool)
#ALL = retorna True, si todos los valores son verdaderos
resultado_all = all([12, "True",[344,12]])
print(f"devuelvo true si todos son verdaderos: {resultado_all}")

#sum = devuelve la suma de todos los numeros que hay en una lista
resultado_suma = sum(numeros)
print(f'yo soy sum y sumos todos los numeros que hay en una lista, ejemplo: {resultado_suma}')
