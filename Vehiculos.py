# Desarrolla un rograma que calcule el importe a pagar por un vehiculo al circular por una autopista. El vehiculo puede ser una bicicleta, una moto, un carro o un camion. 
# Para definir el conjunto de vehiculos deben utilizar una estructura adecuada. El importe de calculara segun los siguientes datos.

# Bicicleta: 100
# Moto y carro pagaran 30 por kilometro
# Camion pagara 30 por kilometro mas 25 por tonelada

# El programa debe solicitar el tipo de vehiculo, la distancia recorrida y en caso de ser un camion, el peso de la carga.

# Entrada de datos:

print("Bienvenido al programa de calculo de importe a pagar por un vehiculo al circular por una autopista")
print("Los tipos de vehiculos son: ")
print("1. Bicicleta")
print("2. Moto")
print("3. Carro")
print("4. Camion")

tipo = int(input("Ingrese el tipo de vehiculo: "))
if tipo == 1:
    importe = 100
elif tipo == 2 or tipo == 3:
    distancia = float(input("Ingrese la distancia recorrida: "))
    importe = 30 * distancia
elif tipo == 4:
    distancia = float(input("Ingrese la distancia recorrida: "))
    peso = float(input("Ingrese el peso de la carga: "))
    importe = 30 * distancia + 25 * peso
else:
    print("Tipo de vehiculo no valido")

print("El importe a pagar por el vehiculo es: ", importe)

