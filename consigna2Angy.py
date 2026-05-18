import math

funcion= int(input("¡Bienvenido al sistema de informacion de funciones lineales!\n Elija a continuacion sobre que tipo de funcion desea trabajar:\n1- Funcion lineal\n2- Funcion cuadratica\nOpcion seleccionada: "))

#def menu2():


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

