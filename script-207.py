#programa: script-207
#programador: heber jafet alvaro ramirez
#descripcion: Dado un número, devuelva el inverso del número
#fecha:07/10/2022

jk=(input('Ingerese número: '))
jm=[]
cifras=len(jk)
inversion=int(jk[cifras::-1])
print('Ingreso el numero: ', jk, 'Su inverso queda: ', inversion) ##Forma 1

for v in jk:
    print(v)
    jm.append(v)
convertor=len(jm)
print(jm[convertor::-1]) #Forma 2