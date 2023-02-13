#programa: script-215
#programador: Heber Jafet Alvaro Ramirez
#decripcion: suma de matrices
#fecha: 19/10/22

dato = []
dato2 = []
resultado = []
fila=int(input('numero de filas: '))
columa= int(input('numero de columnas: '))
for f in range(fila):
    dato.append([]*columa)
    dato2.append([]*columa)
    resultado.append([]*columa)
  
  

print('matriz 1')
for f in range(fila):
  for c in range(columa):
    print('intrudece el valor de:[ ', f, ",", c, "]")
    dato[f].append(int(input()))
print(dato)

print('matriz 2')
for f in range(fila):
  for c in range(columa):
    print('intrudece el valor de:[ ', f, ",", c, "]")
    dato2[f].append(int(input()))
print(dato2)


print('el resultado es:')
for f in range(fila):
  for c in range(columa):
    resultado=dato[f][c]+dato2[f][c]
    print(dato[f][c],dato2[f][c],resultado)