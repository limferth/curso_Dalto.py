#ejercicio 1
# a) Diferencia en porcentaje entre el curso actual y:
#    -el mas rapido de otros cursos 
#   - el mas lento de otros cursos
#   - el promedio de otros cursos

# b) porcentaje de material incervible que se reduce en:
#    - el promedio de los cursos
#    - el curso actual (este curso)

# c) ver 10 horas de este curso a cuentas de otros cursos equivale? y al reves?
#promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4

#dalto curso
dalto_cursos_min = 1.5
#Diferencia de duracion

diferencia_con_min = 100 - (dalto_cursos_min /otros_cursos_min  * 100)
diferencia_con_max = 100 - (dalto_cursos_min *1000 //otros_cursos_max  / 10)
diferencia_con_promedio = 100 - (dalto_cursos_min /otros_cursos_promedio  * 100)

#mostrando las diferencias de duracion (ejercicio A)
print("_________________")
print(f'El curso de dalto dura un {diferencia_con_min} % menos que el mas rapido')
print(f'El curso  de dalto dura un {diferencia_con_max} % menos que el mas lento')
print(f'El curso de dalto dura un {diferencia_con_promedio} % menos que el promedio')
print("_________________")

#ejercicio numero 2
#duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5

#Calculando el porcentaje de tiempo vacio

tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_cursos_min * 1000 // crudo_dalto / 10

# Mostarando la cantidad de espacios vacios que se remueven (EJERCICO B)
print("_________________")
print(f'Un curso promedo elimina un {tiempo_vacio_promedio} % de tiempo  vacio')
print(f'este curso elimino el {tiempo_vacio_dalto} % de tiempo  vacio')
print("_________________")

#Mostrando diferencias si los cursos duraran 10 horas
print("_________________")
print(f'ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_cursos_min / 10} horas de otros cursos')
print(f'ver 10 horas de otros curso equivale a ver {dalto_cursos_min * 100 // otros_cursos_promedio / 10} horas de este curso')
print("_________________")
