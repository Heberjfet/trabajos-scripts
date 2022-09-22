# script 111
# programador: heber jafet alvaro ramirez
# descripcion: una calculadora que suma el iva a un producto y si sobre pasa la cantidad de 1000 se le hara un descuento del 5%
# fecha: 13/09/2022

print('ticket de compra')
iva = strn = (0.16)
descuentoMayor = strn = (0.05)
precio = int(input('ingrese el precio del producto: '))
cantidad = int(input('cantidad que desea comprar: '))
operacion= precio*cantidad
print('precio neto:',operacion)

sumadeliva = operacion*iva
print('iva:',sumadeliva)


ivaMasprecio = operacion + sumadeliva
print('total:',ivaMasprecio)


if ivaMasprecio >=1000:
    descuento =  ivaMasprecio*descuentoMayor
    resolucion = ivaMasprecio - descuento
    print('descuento del 5% por compra mayor a $1000 pesos')
    print('total a pagar:', resolucion)

input()
