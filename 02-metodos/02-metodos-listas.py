#Creando una lista con list
lista = list(["hola", "dalto", 34, 1999, 10])
print(lista)

lista2 = list([ 34, 1999, 10])

#"len" = devuelve la cantidad de elementos de la lista
resultado = len(lista)

print(resultado)

#"len" = devuelve la cantidad de elementos de la lista, se omite crear otra variable 
lista.append("jajaj")

print(lista)

#"len" = agregando a la lista en un indice especifico
lista.insert(2, "toma mama")

print(lista)



#"len" = agregando a la lista en un indice especifico
lista.insert(2, "toma mama")

print(lista)


#"len" = eliminando un elemento de la lista (por su indice)
print(len(lista))

lista.pop(0)

print(len(lista))


#"len" =removiendo un elemento de la lista por su valor
lista.remove("toma mama")

print(lista)


#"sort" = ordenando la lisra (si usamos el parametro reverse = True lo ordena en reversa)
lista2.sort()

print(lista2)

#"reverse" = ordenando la lisra (si usamos el parametro reverse = True lo ordena en reversa)
lista2.reverse()

print(lista2)

#"len" = eliminando todos los elemnetos de la lista
lista.clear()

print(lista)