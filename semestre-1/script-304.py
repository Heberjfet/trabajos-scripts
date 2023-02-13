#programador: heber jafet alvaro ramirez
#script-304
#descripcion: identifica palabaras palindromo
#fecha: 09/11/22
def validacion(texto):
    rever = texto[::-1]
    if texto == rever:
        print("La palabra ingresada si es palindromo!!")
    else:
        print("La palabra ingresada no es palindromo!!")
    
validacion(input('ingrese palabra: ').lower())