import math #Libreria para angulo de funcion lineal
import matplotlib.pyplot as plt #Crea una lista de numeros para el eje x
import numpy as np # agarra la lista de numeros, dibuja los puntos en pantalla y los une con una linea para formar el grafico

try:
    #PRIMER MENU
    funcion= int(input("¡Bienvenido al sistema de informacion de funciones lineales!\n Elija a continuacion sobre que tipo de funcion desea trabajar:\n1- Funcion lineal\n2- Funcion cuadratica\nOpcion seleccionada: "))

    #FUNCION LINEAL
    if funcion == 1:
        m= float(input('--------------------------------------------------------\nDada la ecuacion de funcion lineal "y= mx + b" a continuacion, ingrese los valores correspondientes a cada dato solicitado\nIngrese el valor de m: '))
        bLineal= float(input('Ingrese el valor de "b": '))
            
        if m < 0:
            comportamiento= "Decreciente"
            raizLineal= -bLineal / m
            rango= "-infinito, +infinito"
            angulo= math.degrees(math.atan(m))

        elif m > 0:
            comportamiento= "Creciente"
            raizLineal= -bLineal / m
            rango= "-infinito, +infinito"
            angulo= math.degrees(math.atan(m))

        elif m == 0:
            comportamiento= "Constante"
            rango = f"Solo el valor de b: {bLineal}"
            angulo= 0
            if bLineal == 0:
                raizLineal= "Infinitas raices, la funcion esta sobre el eje x."
            else:
                raizLineal= "La funcion no corta al eje x."

        print("--------------------------------------------------------")
        print(f"La ecuacion ingresada es: y= {m}x + {bLineal}")
        print("Los datos reelevantes de su función son:")
        print(f"- Pendiente: {m}")
        print(f"- Ordenada al origen: {bLineal}")
        print(f"- Raiz: {raizLineal}")
        print(f"- Comportamiento: {comportamiento}")
        print(f"- Angulo: {angulo:.2f}º") #El ".2f" permite mostrar solo 2 decimales despues del punto.
        print("- Dominio: -infinito, +infinito")
        print(f"- Rango: {rango}")

        #SEGUNDO MENU
        opcion = 0
        while opcion != 3:
            print("--------------------------------------------------------")
            opcion= int(input("Elija como desea continuar\n1- Generar grafico de la funcion\n2- Obtener el valor de Y de esa funcion ingresando un valor de X\n3- Salir del programa\nOpcion seleccionada:"))

            if opcion == 1:
                print("Generando grafico...")
                x = np.linspace(-10, 10, 100)
                y = m * x + bLineal
                plt.plot(x, y, label="Función Lineal", color="red") #Traza la linea de la funcion
                plt.show() #Muestra la funcion 
                print("Grafico generado con exito.")

            elif opcion == 2:
                xUsuario= float(input("Ingrese un valor de X:"))
                yUsuario= m * xUsuario + bLineal
                print(f"Para x= {xUsuario}: El valor de Y es: {yUsuario}")

            elif opcion == 3:
                print("Saliendo del programa... ¡Hasta luego!")
            
            else:
                print("Ingrese solo un numero correspondiente a una opcion.")

    #FUNCION CUADRATICA
    elif funcion == 2:
        print('----------------------------------------\nDada la ecuacion de funcion cuadratica "y= ax² + bx + c" a continuacion, ingrese los valores correspondientes a cada dato solicitado.')
        a= float(input("Ingrese el valor de a: "))
        bCuadratica= float(input('Ingrese el valor de "b": '))
        c= float(input('Ingrese el valor de "c": '))

        if a == 0:
            print("El coeficiente 'a' no puede ser 0 en una funcion cuadratica.")
        else:
            vx= -bCuadratica / (2 * a)
            vy= a * (vx)**2 + bCuadratica * vx + c

            if a > 0:
                concavidad= "Concava hacia arriba"
                rango= f"{vy:.2f}, +infinito" #Va del vertice hacia arriba
            elif a < 0:
                concavidad= "Concava hacia abajo"
                rango= f"-infinito, {vy:.2f}" #Va del -infinito hasta el vertice

            discriminante= bCuadratica**2 - 4*a*c

            if discriminante > 0:
                raizD= discriminante**0.5 #Elevar a 0.5 es lo mismo que hacer raiz cuadrada
                raiz1= (-bCuadratica + raizD) / (2*a)
                raiz2= (-bCuadratica - raizD) / (2*a)
                raizCuadratica= f"La funcion tiene 2 raices: x1= {raiz1:.2f} y x2= {raiz2:.2f}"
            elif discriminante < 0:
                raizCuadratica= "La funcion no corta al eje x (sus raices son imaginarias.)"
            else:
                raizCuadratica= f"La funcion solo tiene una sola raiz que coincide con el vertice: {vx}"

            print(f"----------------------------------------\nLa ecuacion ingresada es: y= {a}x² + {bCuadratica}x + c")
            print("Los datos reelevantes de su función son:")
            print(f"- Ordenada al origen: {c}")
            print(f"- Vertice: ({vx:.2f}, {vy:.2f})")
            print(f"- Concavidad: {concavidad}")
            print(f"- Raices: {raizCuadratica}")
            print("- Dominio: -infinito, +infinito") #Para todas las funciones cuadraticas, el dominio es el mismo
            print(f"- Rango: {rango}")

            #SEGUNDO MENU
            opcion = 0
            while opcion != 3:
                print("--------------------------------------------------------")
                opcion= int(input("Elija como desea continuar\n1- Generar grafico de la funcion\n2- Obtener el valor de Y de esa funcion ingresando un valor de X\n3- Salir del programa\nOpcion seleccionada:"))

                if opcion == 1: 
                    print("Generando grafico...")
                    x = np.linspace(-10, 10, 100)
                    y = a * (x**2) + bCuadratica * x + c
                    plt.plot(x, y, label="Función Cuadrática", color="blue") #Traza la linea de la funcion
                    plt.plot(vx, vy, 'ro', label=f"Vértice ({vx:.2f}, {vy:.2f})") #Muestra el vertice
                    plt.show() #Muestra la funcion 
                    print("Grafico generado con exito.")

                elif opcion == 2:
                    xUsuario= float(input("Ingrese un valor de X:"))
                    yUsuario= a * (xUsuario**2) + (bCuadratica * xUsuario) + c
                    print(f"Para x= {xUsuario}: El valor de Y es: {yUsuario:.2f}")

                elif opcion == 3:
                    print("Saliendo del programa... ¡Hasta luego!")
            
                else:
                    print("Ingrese solo un numero correspondiente a una opcion.")
    else:
        print("Ingrese solo un numero correspondiente a una opcion.")

except ValueError:
    print("Ingrese solo valores validos.")