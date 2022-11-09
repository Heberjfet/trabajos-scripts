#programador: heber jafet alvaro ramirez
# script-301
# descripcion: uso de tablas en python
# fecha:08/11/22
usuarios = [[], []]
tamaño = int(input('ingrese tamaño de lista:'))
for i in range(tamaño):
    print("Ingrese los datos de la persona", i + 1)
    nombre = input("Nombre: ")
    identificación = input("Identificación: ")
    usuarios[0].append(nombre)
    usuarios[1].append(identificación)




for i in range(tamaño):
    print("Mostrando los datos de la persona", i + 1)

    print("Nombre:", usuarios[0][i])
    print("Identificación:", usuarios[1][i])








# # mi_tabla= [["juan", "diego"], [21, 22]]
# mi_tabla1= [["carlos", "chepe"], [20, 40]]
# mi_tabla2= [["candy", "martha"], [25, 35]]

# fila= 0
# while fila < len(mi_tabla2):
#     column= 0
#     while column < len(mi_tabla2[fila]):
#         print(mi_tabla2[fila][column])
#         column += 1
#     fila += 1

# # for i in range (len(mi_tabla1)):
# #     for j in range(len(mi_tabla1[i])):
# #         print(mi_tabla1[i][j])

# # for fila in mi_tabla:
# #     for column in fila:
# #         print(column)










# #Obtener el valor de un elemento de una tabla en python

# mi_tabla = [["Jafet", "heber"], [20, 22]]

# print(mi_tabla[0][0])

# print(mi_tabla[-1][1])

# print(mi_tabla[1][0])

# print(mi_tabla[0][1])

# print(mi_tabla[0])






#¿Como crear una tabla en python?

# a = "Tabla en python"
# print(a.center(50, "-"))

# tabla= []

# mi_tabla= [["jafet"], ["heber"], [10, 15]]
# print(mi_tabla[1])