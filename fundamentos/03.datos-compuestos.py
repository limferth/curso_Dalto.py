#DATOS COMPLEJOS
# creando una lista se puede modificar y adicionar

lista = ["limber fernando", "limferth", True, 1.85]

#creando una tupla no se puede modificar, si se puede adicionar
tupla = ("lucas dalto", "saoy lucas", True, 1.85)

lista[3] = "maquinola"

print(lista[3])

#Creando un conjunto (set)

conjunto = {"limber Fer", "limferth", True, 1.85} #en conjunto no podemos tener duplicados, tampoco me muestra el indice

#creando un diccionario
diccionario = {
    'nombre' : "limber fernassssndo",
    'canal' : "no creado",
    'esta_emocionado': True,
    'altura': 1.84,
    'dato_duplicado': "no creado"
}

print(diccionario['nombre'])
