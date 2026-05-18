import math

funcion= int(input("¡Bienvenido al sistema de informacion de funciones lineales!\n Elija a continuacion sobre que tipo de funcion desea trabajar:\n1- Funcion lineal\n2- Funcion cuadratica\nOpcion seleccionada: "))

if funcion == 1:
    m= float(input('----------------------------------------\nDada la ecuacion de funcion lineal "y= mx + b" a continuacion, ingrese los valores correspondientes a cada dato solicitado\nIngrese el valor de m: '))
    bLineal= float(input('Ingrese el valor de "b": '))
        
    if m < 0:
        comportamiento= "Decreciente"
        raizLineal= -bLineal / m
        dominio = "-infinito, +infinito"
        rango= "-infinito, +infinito"
        angulo= math.degrees(math.atan(m))

    elif m > 0:
        comportamiento= "Creciente"
        raizLineal= -bLineal / m
        dominio = "-infinito, +infinito"
        rango= "-infinito, +infinito"
        angulo= math.degrees(math.atan(m))

    elif m == 0:
        comportamiento= "Constante"
        rango = f"Solo el valor de b: {bLineal}"
        angulo= 0
        dominio = "-infinito, +infinito"
        if bLineal == 0:
            raizLineal= "Infinitas raices, la funcion esta sobre el eje x."
        else:
            raizLineal= "La funcion no corta al eje x."

    print(f"----------------------------------------\nLa ecuacion ingresada es: y= {m}x + {bLineal}")
    print("Los datos reelevantes de su función son:")
    print(f"- Pendiente: {m}")
    print(f"- Ordenada al origen: {bLineal}")
    print(f"- Raiz: {raizLineal}")
    print(f"- Comportamiento: {comportamiento}")
    print(f"- Angulo: {angulo:.2f}º") #El ".2f" permite mostrar solo 2 decimales despues del punto.
    print(f"- Dominio: {dominio}")
    print(f"- Rango: {rango}")

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
        print(f"- Dominio: -infinito, +infinito") #Para todas las funciones cuadraticas, el dominio es el mismo
        print(f"- Rango: {rango}")
else:
    print("Ingrese solo un numero correspondiente a una opcion.")
