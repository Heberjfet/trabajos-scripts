#prueba
def suma():
    nunA = int(input('ingrese dato: '))
    numB = int(input('ingrese dato: '))
    sum = nunA + numB
    print ('el resultado es: ',sum)


def resta():
    numA = int(input('ingrese dato: '))
    numB = int(input('ingrese dato: '))
    res = numA - numB
    print('el resultado es: ',res)


def multiplicacion():
    numA = int(input('ingrese dato: '))
    numB = int(input('ingrese dato: '))
    mult = numA * numB
    print('el resultado es: ',mult)

def divicion():
    numA = int(input('ingrese el valor: '))
    numB = int(input('ingrese el valor: '))
    div = numA / numB
    print('el resultado es: ',div)

print("""
s = suma
r = resta
m = multiplicacion
d = divicion
""")
selec = input('seleccione la opereacion a reaalizar: ')

if selec == 's':
    suma()
elif selec == 'r':
    resta()
elif selec == 'm':
    multiplicacion()
elif selec == 'd':
    divicion()