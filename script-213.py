#programa: script-213
#programador: Heber Jafet Alvaro Ramirez
#decripcion: actividad de clase 
#fecha: 16/10/2022
def saludar(*nombres):
  for n in nombres:
    print(n)
saludar('marta','mario', 'pedro')

def sumadelista(lst):
  sum=0
  for elem in lst:
    sum += elem
    return sum

print(sumadelista([5,4,3]))