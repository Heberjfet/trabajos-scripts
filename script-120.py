#programa : script-120
#programador : Heber Jafet Alvaro Ramirez
#descripcion:
#fecha: 21/09/2002

print('calculador de ebullicon')
puntoEbullicion = 100
agua = int(input('ingrese la temperatura:'))
if agua > puntoEbullicion:
    print('por encima del punto de ebullicion')
elif agua == puntoEbullicion:
    print('en el punto de ebullicion')
else:
    print('por debajo del punto de ebullicon')
