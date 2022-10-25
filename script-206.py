#programa: script-206
#programador: heber jafet alvaro ramirez
#descripcion: Obtener la cantidad de los primeros N números múltiplos de 5
#fecha: 07/10/22

n=int(input('numero= '))
list_mul=[]
for i in range (1,n):
    if i % 5 ==0 and n % 5==0:
        list_mul.append(i)
print('Cantidad de multiplos',len(list_mul))
print('Los números multiplo son: ',list_mul)