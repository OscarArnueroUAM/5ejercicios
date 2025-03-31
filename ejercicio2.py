#4. Diseñe un programa que lea un número de tres cifras y determine si es igual al revés del número.

#Entrada de datos
numero = int(input("Ingrese un numero de tres cifras: "))

#Proceso

#Extraer las cifras

cifra1 = numero // 100
resto = numero % 100
cifra2 = resto // 10
cifra3 = resto % 10

#Invertir el numero

numeroInvertido = cifra3 * 100 + cifra2 * 10 + cifra1

#Salida

if numero == numeroInvertido:
    print("El numero es igual al revés")
else:
    print("El numero no es igual al revés")

    