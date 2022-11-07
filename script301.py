#programa: script301.py
#programador: Del carpio Zenteno Anael Guadalupe
#descripcion: Funciones Recursivas
#Fecha: Lunes 7 de Noviembre de 2022

def factorial (numero):
    if numero >1:
        return(numero*factorial(numero-1))
    else:
        return (numero)

numero = int(input('introduzca un numero al que le calculara su factorial: '))
if numero < 0 :
    print('No existe el factorial para su numero negativos') #Condicion para los numeros negativos
elif numero == 0:
    print('El factorial de', numero, 'es 1')