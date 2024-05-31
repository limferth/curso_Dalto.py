# crando un conjunto con set()

conjunto = set(["dalsto 1", "daltso 2"])

print(conjunto)

#metiendo un conjunto dentro de otro conjunto

conjunto1 = frozenset(["lim1", "lim2"])
conjunto2 = {conjunto1, "lim3"}

print(conjunto2)

#teoria de conjuntos 
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1 #tambien funciona  cuando le preguntamos si es <= y viceversa

#verificando si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 >= conjunto1


#verificar si hay algun numero en comun

resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)
