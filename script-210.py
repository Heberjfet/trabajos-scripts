#prueba
def suma():
    nunA = int(input('ingrese dato: '))
    numB = int(input('ingrese dato: '))
    sum = nunA + numB
    print ('el resultado es: ',sum)


def resta():
    numA = int(input('ingrese dato'))
    numB = int(input('ingrese dato: '))
    res = numA - numB
    print('el resultado es: ',res)


def multiplicacion():
    numA = int(('ingrese dato: '))
    numB = int(('ingrese dato: '))
    mult = numA * numB
    print('el resultado es: ',mult)

print("""
s = suma
r = resta
m = multiplicacion
d = divicion
""")
selec = input('seleccione la opereacion a reaalizar: ')

if selec == 's':
    suma()
else selec == 'r':
    resta()