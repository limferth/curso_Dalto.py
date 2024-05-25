# ejercicio uno
edad = 17
if edad >= 18:
    print("podes pasar cjdo")
else: 
    print("no podes pasar")

print("no forma parte de ninguna condicion")
#ejercicio 2

contrasena_almacenada = "todosPodemos"
contrasena_escrita = "todosPodemos"

if contrasena_almacenada == contrasena_escrita:
    print("INICIANDO SESION")
else:
    print("contrasena incorreta, INTENTE DE NUEVO")


#ELSE IF e elif anidados
ingreso_mensual = 15000
gasto_mensual = 15000
ahorro_obligatorio = 8000

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual > 8000:
        print("estas bien en culquier parte del mundo")
    elif ingreso_mensual - gasto_mensual <= 0:
        print("estas en deficit")
    else: 
        print("estas bien en culquier parte del mundo, pero gastas mucho voludo")
elif ingreso_mensual > 1000:
    print("estas bien economicamente en latianomeria")
elif ingreso_mensual > 500:
    print("Estas bien en bolivia")
else:
    print("estas quebrado")