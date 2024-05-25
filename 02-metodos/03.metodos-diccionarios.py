#DIC METHODS
diccionario = {
    "nombre" : "limfer fernando",
    "apellido" : 'Alanoca plata',
    "subscript": 0
}

#keys = devuelve las claves (tambien nos sirve para iterar)
clave = diccionario.keys()
print(clave)


#get = obteniedno un elemento con get, y si no encuentra nada el programa continua 
llamando_con_get = diccionario.get("nombre")
print(llamando_con_get)

#get = obteniedno un elemento con get, y si no encuentra nada el programa continua 
diccionario.pop("apellido")
print(diccionario)

#get = obteniendo un diccionario dict_items iterable
diccionario_iterable = diccionario.items()
print(diccionario_iterable)

#get = eliminando todo del diccionario 
diccionario.clear()
print("elimino todo del diccionario",diccionario)
