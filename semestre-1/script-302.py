#programador: heber jafet alvaro ramirez
#
#
#

def validador(ing):
    lit=["a","e","i","o","u"]
    dato=[]
    dato.append(ing)
    for column in dato:
        print(column)
    for colum in lit:
        if column[0] == colum[0]:
            print('verdadero')
        else:
            print('falso')



validador(input('ingrese dato: '))
