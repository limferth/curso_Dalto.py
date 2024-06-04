#craando una funcion que nos devuelva los numero primos
#entre cero y el argumento quye le pasemos


#cramos una funcion que verifique si un numero es primo
def es_primo(num):
    #verificamos que el numero pasado no pueda dividirse por ningun numero entre 2 y ese mismo numero -1
    for i in range(2,num-1):
        #si es divisible por alguno retornamos false
        if num%i==0: return False
    #si termina el bucle, significa que es no fue divisible entonces es primo
    return True


##creamos una funcion que retorne una ,lista con todos los primos
def primos_hasta(num):
    #creamos la lista
    primos = []
    for i in range(1,num + 1):
        #verificamos si el valor es primo
        resultado = es_primo(i)
        #rn caso de que lo sea agregamos a la lista
        if resultado == True: primos.append(i)
    #devolvemos la lista
    return primos


resultado = primos_hasta(13)
print(resultado)