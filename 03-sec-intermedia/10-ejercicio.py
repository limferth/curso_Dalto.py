#ejercicio

#1 Alumno es profesor
#1 Alumno es asistente
#A) pedir la edad de los companeros que vinieron hoy a clase y ordenar los datos de menor a mayor
#B) el mayor de la clase es el profesor y el menor elo asistente: (Quien es quien)


#pedri el nombre y la edad de los compaNeros que vinieron hoy a clase

def obtener_companeros(cantidad_de_companeros):
    compeneros = []
    #ejecutamos un for para pedir informacion de cada companero
    for i in range(cantidad_de_companeros):
        nombre = input("ingrese el nombre del companero: ")
        edad = int(input("ingrese la edad del companero: "))
        companero = (nombre, edad)
        #agregando la informacion a la lista
        compeneros.append(companero)
    #ordenandolos de menor a mayor segun su edad
    compeneros.sort(key=lambda x:x[1])
    
    #companero x deviuelve una tupla con (nombre y edad) y despues accedemos al nombre
    #para definir para definir al asistente del profesor
    asistente = compeneros[0][0]
    profesor = compeneros[-1][0]
    
    #retornamos una tupla
    return asistente,profesor


#desempaquetamos la que nos retorna la funcion
asistente,profesor = obtener_companeros(5)

#mostramos el resultado con print
print(f"el profesor es: {profesor} y e asistente es: {asistente}")