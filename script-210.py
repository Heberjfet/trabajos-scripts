def suma():

numA = input('ingrese valor: ')

numB = input('ingrese valor: ')

sum = numA + numB

print(sum)

suma()


def resta():

numA = input('ingresa valor: ')

numB = input('ingresa valor: ')

res = numA - numB

print(res)

resta()


def multiplicacion():

numA = ('ingresa valor: ')

numB = ('ingresa valor: ')

multi = numA * numB

print(multi)

multiplicacion()


def divicion():

numA = ('ingresa valor: ')

numB = ('ingresa valor: ')

div = numA / numB

print(div)

divicion()


print("""

s = suma

r = resta

m = multiplicacion

d = divicion

""")

ope = input('ingrese la operacion deseada: ')

if ope == 's':

suma()

elif ope == 'r':

resta()

elif ope == 'm':

multiplicacion()

elif ope == 'd':

divicion()


