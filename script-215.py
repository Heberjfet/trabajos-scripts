#programa: script-215
#programador: Heber Jafet Alvaro Ramirez
#decripcion: matrices
#fecha: 19/10
print('matris 1')
dato = []
dato2 = []
resultado = []
for f in range(3):
  dato.append([])
  dato2.append([])
  resultado.append([])
for f in range(3):
  for c in range(3):
    print('intrudece el valor de:[ ', f, ",", c, "] el cierre de corchete")
    dato[f].append(int(input()))
print(dato)

print('matris 2')
for f in range(3):
  dato2.append([])
for f in range(3):
  for c in range(3):
    print('intrudece el valor de:[ ', f, ",", c, "] el cierre de corchete")
    dato2[f].append(int(input()))
print(dato2)
#print(resultado)
for s in range(0,0):
  suma(dato,dato2)
  print(s)