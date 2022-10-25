#programa: script-209
#programador: heber jafet alvaro ramirez
#descripcion: Estructura y manejo de las FUNCONES y del RETURN
#fecha:06/10/22

def mensaje(): #Funciones: Son un procedimiento espesifico, invocar muchas veces y reduce el espacio del programa
    print('ingrese siguiente valor')
    print('Muy bien hecho')
print('Comenzamos aquí')
mensaje()
mensaje()
mensaje()
print('El final es aqui') #La funcion se ejecuta en la parte donde fue invoca y las veces de esta, hasta que ya no aiga mas, llegando al fin

def saludar():
    print("Buenos dias")
print('Hola')
saludar()

def suma():
    print('Dame un número')
    num1= int(input())
    print('Dame otro número')
    num2= int(input())
    resultado=num1+num2
    print('El resultado es: ',resultado)
print('Operacion de suma')
suma()