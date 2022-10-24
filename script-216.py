#programa: script-215
#programador: Heber Jafet Alvaro Ramirez
#decripcion: matrices
#fecha: 19/10

cadena1 = 'hola a todos'.title()
cadena2 = "heber jafet es una prueba de front".upper()
cadena3 = 'edad:{0}, peso: {peso}'.upper()
cadena4 = '1234'
cadena5 = 'www.hebrdiafet@'
cadena6 = ("edad:"," ")
dato = "20"
# print(cadena1.capitalize())
# print(cadena2.capitalize())
# print(cadena2.lower())
# print(cadena1.upper())
# print(cadena2.swapcase())
print(cadena1.center(50,"-"))
# print(cadena2.center(50,"°"))
# print(cadena2.ljust(30,"*"))
# print(cadena3.rjust(30,'-'))
# # print(str(cadena3).zfill(25))
# pru = str(input('nombre de usuario: '))
# print(pru.count('e'))
# print(cadena2.find('una',10,20))
# print(cadena2.startswith('Heber'))
# print(cadena3.isalnum())
print(cadena3.isalpha())
print(cadena4.isdigit())
print(cadena1.islower())
print(cadena2.isupper())
print(cadena1.isspace())
print(cadena2.istitle())
print(cadena3.format('20', PESO = 70))
print(cadena5.strip('@'))
print(cadena5.lstrip('w'))
sus = dato.join(cadena6)
print(sus)
tupla = ('http//www.python.com'.partition('www.'))
print(tupla)
protocolo, separador, dominio = tupla
print("protocolo: {0}\n""separador: {1}\n""dominio: {2}".format(protocolo,separador,dominio))
keyword = 'datos-edad,altura,peso'.split('-')
print(keyword)