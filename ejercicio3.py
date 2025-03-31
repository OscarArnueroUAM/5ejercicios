'''3. Un supermercado ha puesto en oferta la venta al por mayor de cierto producto, 
ofreciendo un descuento del 15% por la compra de más de 3 docenas y 10% en caso contrario. 
Además, por la compra de más de 3 docenas se obsequia una unidad del producto por cada docena en exceso sobre 3. 
Diseñe un programa que determine el monto de la compra, el monto del descuento, el monto a pagar y el número de unidades de obsequio por la 
compra de cierta cantidad de docenas del producto.'''

#Entrada de datos

while True:
    try:
        cantidad = int(input("Ingrese la cantidad de docenas de productos: "))
        if cantidad <= 0:
            print("La cantidad debe ser mayor que 0. Intente de nuevo.")
            continue
        break
    except ValueError:
        print("Entrada no válida. Asegúrese de ingresar números correctos.")

#Proceso

precio = 100
docena = 12
subtotal = precio * cantidad * docena
descuento = 0
obsequio = 0
iva = subtotal * 0.15

if cantidad >= 3:
    descuento = subtotal * 0.15
    obsequio = (cantidad - 3) * docena
else:
    descuento - subtotal * 0.10

total = subtotal - descuento + iva

#Salida

print("El subtotal es:", subtotal)
print("El descuento es:", descuento)
print("El total a pagar es:", total)