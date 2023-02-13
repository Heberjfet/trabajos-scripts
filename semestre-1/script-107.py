# script 107
# programador: heber jafet alvaro ramirez
# descripcion: programa no.1
# fecha: 07/09/2022
import math

print('ecuacion cuadratica')
valorA=int(input('ingresa un valor '))
valorB=int(input('ingresa el valor:'))
valorC=int(input('ingresa el valor:'))
ecuacion=(valorB**2)-(4*(valorA*valorC))
if ecuacion < 0:
    print('son numeros reales')
elif(ecuacion == 0):
    print ('es un numero buena onda')
else:
    print('es un numero imaguinario')


