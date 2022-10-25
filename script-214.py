#programa: script-214
#programador: Heber Jafet Alvaro Ramirez
#decripcion: numeros primos
#fecha: 16/10/2022


def is_prime(numero):
  for i in range(2,numero): 
    if (numero%i) == 0:
      print(i, 'es primo')
    else:
      print(i, 'no es primo')

is_prime(int(input('ingresa el valor: ')))