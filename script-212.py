#escribir y probar una funcion que reciba un año como argumento y devuelve true si el año es un año bisisesto, o flase si no lo es.enviar varios años hasta que se teclee un valor 0
#programa: script-211
#programador: Heber Jafet Alvaro Ramirez
#decripcion: años viciestos
#fecha: 16/10/2022

print('calculador de año biciestos')

info =int(input('ingrese el año:'))
datos=()
cero=1
while info == 0:
    # año=int(input('ingrese año:'))
    datos =list(datos)
    datos.append(info)
    print(datos)
    if datos == 0:
        break

def años():
    if años % 4 == 0:
        print('es aun año biciesto')
    else:
        print('no es un año biciesto')