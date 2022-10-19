#programa: script-214
#programador: Heber Jafet Alvaro Ramirez
#decripcion: numeros primos
#fecha: 16/10/2022


def numeros_primos(numero):
  for i in range(1, int(numero / 2)):
    if (numero % i) == 0:
      print(i, 'es primo')
    else:
      print(i, 'no es primo')


numeros_primos(int(input('ingresa el valor: ')))