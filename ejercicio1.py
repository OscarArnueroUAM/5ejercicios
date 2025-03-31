#2. Escribir un programa que permita emitir la FACTURA correspondiente, 
# a una compra de un artículo determinado, del que se adquieren una o varias unidades. 
# El IVA a aplicar es de 15% y si el Sub Total (precio de venta por cantidad), es mayor de 1000, se aplicará un descuento del 12%.


# Entrada de datos
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio <= 0:
            print("El precio debe ser mayor que 0. Intente de nuevo.")
            continue
        cantidad = int(input("Ingrese la cantidad de productos: "))
        if cantidad <= 0:
            print("La cantidad debe ser mayor que 0. Intente de nuevo.")
            continue
        break
    except ValueError:
        print("Entrada no válida. Asegúrese de ingresar números correctos.")

subtotal = precio * cantidad

# Proceso
iva = subtotal * 0.15
if subtotal > 1000:
    descuento = subtotal * 0.12
else:
    descuento = 0

total = subtotal + iva - descuento

# Salida
print("El subtotal es:", subtotal)
print("El IVA es:", iva)
print("El descuento es:", descuento)
print("El total a pagar es:", total)
