# script 116
# programador: heber jafet alvaro ramirez
# descripcion: pide 10 numeros al usuario y calcula la media
# fecha: 13/09/2022

print('calculador de media')
cantidades = []
for nume in range (0,10):
    cantidades.append(int(input('ingrese los numeros: ')))

media = sum(cantidades)
divicion = (media / 10)
print('la media es: ',divicion)

input()
print('by jafet')