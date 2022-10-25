#programa: script-215
#programador: Heber Jafet Alvaro Ramirez
#decripcion: matrices
#fecha: 24/10/22

h = 'usuario'.upper()
print(h.center(50, "-"))


def usuario(dato):
    validacion2 = dato.isalnum()
    conte = len(dato)
    if validacion2 != True:
        print('solo se permiten letras y numeros')
    if conte < 6:
        print('el usuario minimo es de 6 caracteres')
    if conte > 12:
        print('el usuario solo puede contener max 12 carecteres')


# usuario(input('nombre de usuario: '.title()))


def contraseña(dato1):
    conta = len(dato1)
    conpro = dato1.isalpha()
    mayusculas = dato1.islower()
    num = dato1.isdigit()
    if conta < 8:
        print('anañade mas caracteres')
    elif conpro == True :
        print('añade un numero')
    elif mayusculas != False:
        print('añade una letra mayuscula')
    elif num == True:
        print('añade letras y numeros')
    


contraseña(input('ingresa la contraseña: '))
