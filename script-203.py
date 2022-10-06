#programa: script-128
#programador: Heber Jafet Alvaro Ramirez
#decripcion: cuantos digitos tiene un numero
#fecha: 05/10/2022
print('cuantos digitos tiene un numero tiene un numero')

n = int(input('dijite un numero: '))
c = 0
while n > 0:
  n = n // 10
  c = c + 1
print('la cantidad de digitos es: ',c)
