'''
5. Se desea escribir un programa para el cálculo del área de diversas superficies: cuadrado, rectángulo, círculo, triángulo y trapecio. 
El programa mostrará al inicio el siguiente menú:
Seguidamente leerá de la entrada estándar un valor que estará comprendido entre 1 y 5, indicando el tipo de superficie cuya área se desea calcular.  
El programa leerá entonces los datos que necesite para calcular el área en cuestión.  El resultado se mostrará en la salida estándar, tras lo cual el programa terminará.
-	Implementa estructuras repetitivas de tal forma que los programas se ejecuten mientras el usuario lo desea.

'''

#Entrada de datos

while True:
    try:
        print("Menu de opciones")
        print("1. Cuadrado")
        print("2. Rectangulo")
        print("3. Circulo")
        print("4. Triangulo")
        print("5. Trapecio")
        print("6. Salir")
        opcion = int(input("Ingrese la opcion deseada: "))
        if opcion < 1 or opcion > 6:
            print("Opcion no valida. Intente de nuevo.")
            continue
        if opcion == 6:
            break
        break
    except ValueError:
        print("Entrada no válida. Asegúrese de ingresar números correctos.")

#Proceso

if opcion == 1:
    lado = float(input("Ingrese el lado del cuadrado: "))
    area = lado ** 2
    print("El area del cuadrado es:", area)
elif opcion == 2:
    base = float(input("Ingrese la base del rectangulo: "))
    altura = float(input("Ingrese la altura del rectangulo: "))
    area = base * altura
    print("El area del rectangulo es:", area)
elif opcion == 3:
    radio = float(input("Ingrese el radio del circulo: "))
    area = 3.1416 * radio ** 2
    print("El area del circulo es:", area)
elif opcion == 4:
    base = float(input("Ingrese la base del triangulo: "))
    altura = float(input("Ingrese la altura del triangulo: "))
    area = base * altura / 2
    print("El area del triangulo es:", area)
elif opcion == 5:
    base1 = float(input("Ingrese la base mayor del trapecio: "))
    base2 = float(input("Ingrese la base menor del trapecio: "))
    altura = float(input("Ingrese la altura del trapecio: "))
    area = (base1 + base2) * altura / 2
    print("El area del trapecio es:", area)

#Salida

print("Fin del programa")