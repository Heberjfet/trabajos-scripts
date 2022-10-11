#prueba
def suma():
    nunA = input('ingrese dato: ')
    numB = input('ingrese dato: ')
    sum = nunA + numB
    print (sum)
    suma()

def resta():
    numA = input('ingrese dato')
    numB = input('ingrese dato: ')
    res = numA - numB
    print(res)
    resta()

def multiplicacion():
    numA = ('ingrese dato: ')
    numB = ('ingrese dato: ')
    mult = numA * numB
    print(mult)
    multiplicacion()



print("""
s = suma
r = resta
m = multiplicacion
d = divicion
""")
selec = input('seleccione la opereacion a reaalizar: ')
if selec == 's':
    suma()
