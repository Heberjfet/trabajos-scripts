#programador: heber jafet alvaro ramirez
#script-306
#descripcion: imprime los numeros en forma de un histograma 
#fecha: 09/11/22

def histograma(numeros):
    aste =''
    # numeros.append(his)
    for i in numeros:
        print(aste.center(i,"*"))
numeros = [2,3,4,5]
histograma(numeros)