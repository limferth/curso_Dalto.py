# Metodos de cadenas
cadena1 = "soY fEr LimbEr"
cadena2 = "Bienvenido,maquinola,a,la,joda"

# "upper" = convierte a mayuscaluas
mayus = cadena1.upper()

# "upper" = convierte a minusculas
minusculas = cadena1.lower()

# "capitalize" = convierte la primera letra en masyucula
primera_letra_mayuscula = cadena1.capitalize()

print(primera_letra_mayuscula)
# "find" = buscamos una cadena en otra cadena, si no encuentra nos manda -1
busqueda_find = cadena1.find("Y")
print(busqueda_find)

# "index" = buscamos una cadena dentro de otra cadena igual que capitalize, si no encuentra nos lanzza un error
busqueda_index = cadena1.index("L")
print(busqueda_index)

# "isnumeric" = si esnumerico, devolvemos true, si no lo es devolvemos false
es_numerico = cadena1.isnumeric()
print(es_numerico)

# "isalpha" = si es alfa numerico devolvemos truw, sino devolvemos false
es_alfa_numerico = cadena1.isalpha()
print(es_alfa_numerico)

# "index" = Contamos la cantidad de concidencias de una cadena dentro de otra cadena, devolvemos la cantidad de coincidencias
contar_coincidencias = cadena1.count("E")
print("las coincidencias de E =", contar_coincidencias)

# "len" = contamos cuantos caracteres tiene una cadena, len es una funcion
contar_caracteres = len(cadena1)
print(contar_caracteres)

# "startswith" = verificamos si una cadena empieza con otra cadena dada, sis es asi devuelve true
empieza_con = cadena1.startswith("soY")
print(empieza_con)

# "index" = verificamos si una cadena termina con otra cadena dada, sis es asi devuelve true
termina_con = cadena1.endswith("LimbErth")
print("termina con LimbEr =", termina_con)

# "replace" = reempleza un pedazo de la cadena dada, por otra dada, siempre y cuando encuentre coincidencias
cadena_nueva = cadena1.replace("soY fEr LimbEr", "SOY LIMBER FERNANDO ")
print("REMPLAZAMOS soY fEr LimbEr con =", cadena_nueva)

# "replace" = separar cadenas con la cadena que le pasemos
cadena_separada = cadena2.split(",")
print(cadena_separada)
