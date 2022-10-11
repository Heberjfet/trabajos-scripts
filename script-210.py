#prueba
def suma():
    nunA = input('ingrese dato: ')
    numB = input('ingrese dato: ')
    sum = nunA + numB
    print (sum)
    suma()

print("""
s = suma
r = resta
m = multiplicacion
d = divicion
""")
selec = input('seleccione la opereacion a reaalizar: ')
if selec == 's':
    suma()
