try:
    print("¡Bienvenido! Este sistema le permitira concocer el plan mas economico segun las horas que requiera contratar.")
    horas= float(input("Ingrese la cantidad de horas mensuales a contratar (0 a 50):  "))

    costoA= 40 * horas + 200
    costoB= 70 * horas + 50
    costoC= -2 * (horas**2) + 80 * horas + 100

    if horas >= 0 and horas <= 50:
        if horas >= 0 and horas <= 5:
            print(f"El plan más económico es el: PLAN LINEAL B, con un costo total de ${costoB}")
        elif horas > 5 and horas <= 17:
            print(f"El plan más económico es el: PLAN LINEAL A, con un costo total de ${costoA}")
        elif horas > 17 and horas <= 41.2:
            print(f"El plan más económico es el: PLAN CUADRÁTICO C, con un costo total de ${costoC}")
        else:
            print("Para más de 41.2 horas el Plan C no está disponible por dar costos negativos.")
            print(f"El plan activo más conveniente en este tope es el: PLAN LINEAL A, con un costo total de ${costoA}")

    else:
        print("Error: Ingrese un valor entre 0 y 50 horas")


except ValueError:
    print("Error: Ingrese solo valores numéricos válidos.")