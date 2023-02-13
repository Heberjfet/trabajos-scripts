#programa: script-128
#programador: Heber Jafet Alvaro Ramirez
#decripcion: calcular el promedio de 3 calificaciones si es de un estudiante de genero masculino si su calf>= 8 aprueba, si es mujer calf>=6 aprueba.
#Fecha: 29/09/22
print('comparador de calificiones')
calf1 = int(input('calificacion 1: '))
calf2 = int(input('calificacion 2: '))
calf3 = int(input('calificacion 3: '))
genero = input('genero: ')
sum = calf1 + calf2 + calf3
pro = sum / 3
if pro >= 8 and genero != 'm':
    print('aprobo la materia')
elif pro < 8 and genero == 'm':
    print('estas reprobado')

elif pro >= 6 and genero == 'f':
    print('aprobo la materia')
elif pro < 6 and genero == 'f':
    print('reprobaste la materia')
