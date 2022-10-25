#programa: script-207
#programador: heber jafet alvaro ramirez
#descripcion: Indicar si un número es cubo perfecto. Se dice que un número es cubo perfecto si al sumar los cubos de sus dígitos dan el mismo número
#fecha:07/10/2022

n1=int(input('Ingrese numero: '))
list_digitos=[]
list_cubos=[]

a=[int(t) for t in str (n1)]
print(a)
for k in a:
    list_digitos.append(k)
for v in list_digitos:
    cubos= v**3
    list_cubos.append(cubos)
    cubo2=sum(list_cubos)
    print(cubo2)
if cubo2== n1:
    print('cubo perfecto')
else:
    print('intente con otro número')

##Se entendia que: elevar los digitos al cubo y sumarlos daba igual a el número ingresado##
#a=[int(t) for t in str (n1)] ---Para obtener los digitos de un número ingresado
#Round: Para redondear
## La imporatancia de saber usar las listas y el uso de FOR






