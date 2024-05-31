#creando una funcion simple

def saludar():
    print("hola limber, mi maestro como andas")
    
#saludar()

#CREANDO UNA FUNCION QUE TENGA PARAMETROS
def Saludar1(nombre,sexo):
    sexo = sexo.lower()
    if(sexo == "mujer"):
        adjetivo = "reina"
    elif(sexo == "hombre"):
        adjetivo = "titan"
    else:
        adjetivo = "amor"
        
    print(f'hola {nombre}, mi {adjetivo} como andas')

Saludar1("limferth", "mujer")

#creando una funcion que nos retorne valores aleatorios para contrasena

def crear_contrasena_ramdom(num):
    chars = "asdfjdfjdjf"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num -2
    c2 = num 
    c3 = num - 5
    contrasena = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contrasena


password = crear_contrasena_ramdom(16)
frase = f"tu nueva contrasena es: {password}"
print(frase)

#forma no optima de sumar valores
def suma(a,b):
    return a+b
resultado_ultra = suma(5,6)
print(resultado_ultra)

#utilizando el parametro args
def suma(nombre,*numeros):
    return f'{nombre} la suma de tus numeros es igyual a : {sum(numeros)}'

resultado = suma("limber", 4,5,16,2,2)
print(resultado)