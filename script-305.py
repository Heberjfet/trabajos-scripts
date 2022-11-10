#programador: heber jafet alvaro ramirez
#script-305
#descripcion: convierte un numero a caracter
#fecha: 09/11/22

def n_carater(numby):
    carater = []
    carater.append(input('ingrese caracter: '))
    a = numby * carater
    # lst_str = str(a)[1:-1]
    # print(lst_str)
    print(*a)

n_carater(int(input('ingrese un numero: ')))