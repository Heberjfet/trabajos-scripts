#programa: script-211
#programador: Heber Jafet Alvaro Ramirez
#decripcion: años viciestos
#fecha: 16/10/2022

print('calculador de año biciestos')

info =int(input('ingrese el año:'))
ex=0
while info == 0:
    input('ingrese el año')

def años():
    if años % 4 == 0:
        print('es aun año biciesto')
    else:
        print('no es un año biciesto')
