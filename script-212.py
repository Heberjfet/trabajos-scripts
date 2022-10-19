#escribir y probar una funcion que reciba un año como argumento y devuelve true si el año es un año bisisesto, o flase si no lo es.enviar varios años hasta que se teclee un valor 0
#programa: script-212
#programador: Heber Jafet Alvaro Ramirez
#decripcion: años viciestos
#fecha: 16/10/2022

print('calculador de año biciestos\n 0 = salir')

datos=[]
while datos != 0:
    info =int(input('ingrese el año:'))                     
    if info == 0:
        break
    # datos =list(datos)
    datos.append(info)
    if info % 4 == 0 and (info % 100 != 0 or info % 400 == 0):
        print('es aun año biciesto')
    else:
        print('no es un año biciesto')
    # print(datos)
    