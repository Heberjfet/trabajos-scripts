#programa: script-204
#programador: heber jafet alvaro ramirez
#descripcion: Dados 2 números diga si son amigos, recuerda que dos números son amigos si la suma de sus divisores de uno de ello es igual al otro y viceversa
#fecha de entrega: 05/10/22


n1=int(input('numero1: '))
n2=int(input('numero2: '))


list_divisores=[]
list_divisores2=[]

for t in range (1,n1):
    if n1 % t ==0:
        list_divisores.append(t)
        suma1=sum(list_divisores)
for i in range (1,n2):
    if n2 % i ==0:
        list_divisores2.append(i)
        suma2=sum(list_divisores2)

if suma1==n2 and suma2==n1:
    print('Son amigos')
else:
    print('No son amigos') 
#list-divisores.append(t), es para sumar los elemntos de la lista
#Para append se usa parentesis
#Mod (%) son para el residuo de las divisiones
#sum, para sumar
#Las variables t, i, seran almacenedores de los rangos
