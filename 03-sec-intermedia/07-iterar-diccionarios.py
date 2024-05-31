#iterando diccionarios
diccionarios = {
    "nombre": "limber",
    "apellido": "alanoca",
    "subs": 10000
}

#recooriendo diccionarios para obtener las claves
for key in diccionarios:
    key
    print(f'la clave es : {key}')


#recoocriendo diccionario con items() para obtener las claves y los valores
for datos in diccionarios.items():
    key = datos[0]
    valor = datos[1]
    print(f'la clave es : {key} u el valor es : {valor}' )