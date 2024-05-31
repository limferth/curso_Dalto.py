#creando diccionarios con dict()
diccionario = dict(nombre = "limber", apellido="alanoca")



#las listas no pueden ser claves
diccionario = {("dalto", "genio"):"sdsds"}

diccionario1 = {frozenset(["ddalto", "ggenio"]):"sdsdffs"}

#creando diccionarios con fromkeys() valor por defecto none
diccionario= dict.fromkeys("nombre", "apellido")

#creando diccionarios con fromkeys() cambiando el valor por defecto a nose
diccionario1= dict.fromkeys(["nombre", "apellido"], "no se")


print(diccionario)
print(diccionario1)