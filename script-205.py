#programa: script-128
#programador: Heber Jafet Alvaro Ramirez
#decripcion: los numero pares dentro de un rango inicial y final
#fecha: 05/10/2022

rI = int(input('ingrese el rango inicial: '))
rF = int(input('ingrese el rango final: '))
repo = []
for i in range (rI,rF + 1):
    repo.append(i)
    rI % i == 0
    print('es par',repo)
