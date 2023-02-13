




contenido = open("nombreABC.txt", "r")
contador = 1

for linea in contenido:
    print("linea",contador, ":", linea)
    contador += 1

contenido.close()
