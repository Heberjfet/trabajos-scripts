#
#
#
#

nombres = ["juan","heber","alvaro","ramirez"]
archivo = open("nombreABC.txt","w")

for nombre in nombres:
    archivo.write(nombre + "\n")

archivo.close()