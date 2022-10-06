#programa: script-128
#programador: Heber Jafet Alvaro Ramirez
#decripcion:
#fecha: 05/10/2022

from multiprocessing import Value


rI = int(input('ingrese el rango inicial: '))
rF = int(input('ingrese el rango final: '))
repo = []
for i in range (rI,rF + 1):
    repo.append(i)
    rI % i == 0
    print('es par',repo)
