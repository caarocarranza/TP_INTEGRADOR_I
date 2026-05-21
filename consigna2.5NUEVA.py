import matplotlib.pyplot as plt #Crea una lista de numeros para el eje x
import numpy as np # agarra la lista de numeros, dibuja los puntos en pantalla y los une con una linea para formar el grafico

try:
    #PRIMER MENU
    print("¡Bienvenido al sistema de informacion de costos de la empresa!")
    print("Se informa que todos los planes de desarrollo operan bajo un TOPE MÁXIMO de 50 horas de trabajo mensuales por cliente (0 <= x <= 50).")
    print("El sistema bloqueará o alertará cualquier valor fuera de este rango.")
    print("--------------------------------------------------------")

    plan= int(input("Elija a continuacion sobre que tipo de plan desea trabajar:\n" 
                    "1- Plan lineal A\n" 
                    "2- Plan lineal B\n"
                    "3- Plan cuadratico C (con descuento por hora utilizada)\n"
                    "Opcion seleccionada: "))

    #PLAN LINEAL A
    if plan == 1:
        m= 40 #Precio por hora
        bLineal= 200 #Costo fijo inicial    
        horas= int(input("Ingrese la cantidad de horas de uso del plan A(de 0 a 50): "))
        
        if horas < 0 or horas > 50:
            print("Error: La cantidad de horas debe estar entre 0 y 50.")
        else:
            costoTotal= m * horas + bLineal

            print("--------------------------------------------------------")
            print("PRESUPUESTO PERSONALIZADO:")
            print(f"Para un uso de {horas} horas, el costo total del plan es de: ${costoTotal}")
            print("Detalles:")
            print(f"- Costo fijo inicial: ${bLineal}")
            print(f"- Precio por hora de servicio: ${m}")
            print(f"- Horas utilizadas: {horas}")
            print(f"- Costo por hora: ${m * horas}")

            #SEGUNDO MENU A
            opcion = 0
            while opcion != 2:
                print("--------------------------------------------------------")
                opcion = int(input("Elija cómo desea continuar\n"
                                    "1- Generar gráfico de este plan\n"
                                    "2- Salir del programa\n"
                                    "Opcion seleccionada: "))
                if opcion == 1:
                    print("Generando grafico...")
                    x = np.linspace(0, 50, 100)
                    y = m * x + bLineal

                    # Traza la línea del Plan A
                    plt.plot(x, y, label="Costo Plan A (40x + 200)", color="blue")

                    # Dibuja el punto de consumo del cliente en color rojo ('ro')
                    plt.plot(horas, costoTotal, 'ro', label=f"Tu Consumo (${costoTotal:.2f})")

                    plt.xlim(0, 50)  # Corta el eje X exacto en 50
                    plt.ylim(0, 2400) # Ajusta el eje Y más alto porque el Plan A sube hasta 3550
                    plt.xlabel("Horas de Trabajo")
                    plt.ylabel("Costo Total ($)")
                    plt.title("Evolución de Costos - Plan A")
                    plt.grid(True, linestyle="--")
                    plt.legend()
                    plt.show() #Muestra la funcion 
                    print("Grafico generado con exito.")
                elif opcion == 2:
                    print("Saliendo del programa... ¡Hasta luego!")
                else:
                    print("Ingrese solo un numero correspondiente a una opcion.")

    #PLAN LINEAL B
    elif plan == 2:
        m= 70 #Precio por hora
        bLineal= 50 #Costo fijo inicial    
        horas= int(input("Ingrese la cantidad de horas de uso del plan B (de 0 a 50): "))
        if horas < 0 or horas > 50:
            print("Error: La cantidad de horas debe estar entre 0 y 50.")
        else:
            costoTotal= m * horas + bLineal

            print("--------------------------------------------------------")
            print("PRESUPUESTO PERSONALIZADO:")
            print(f"Para un uso de {horas} horas, el costo total del plan es de: ${costoTotal}")
            print("Detalles:")
            print(f"- Costo fijo inicial: ${bLineal}")
            print(f"- Precio por hora de servicio: ${m}")
            print(f"- Horas utilizadas: {horas}")
            print(f"- Costo por hora: ${m * horas}")

        #SEGUNDO MENU B
        opcion = 0
        while opcion != 2:
            print("--------------------------------------------------------")
            opcion = int(input("Elija cómo desea continuar\n"
                                "1- Generar gráfico de este plan\n"
                                "2- Salir del programa\n"
                                "Opcion seleccionada: "))
            if opcion == 1:
                print("Generando grafico...")
                x = np.linspace(0, 50, 100)
                y = m * x + bLineal

                # Traza la línea del Plan B
                plt.plot(x, y, label="Costo Plan B (70x + 50)", color="orange")

                # Dibuja el punto de consumo del cliente en color rojo ('ro')
                plt.plot(horas, costoTotal, 'ro', label=f"Tu Consumo (${costoTotal:.2f})")

                plt.xlim(0, 50)  # Corta el eje X exacto en 50
                plt.ylim(0, 3700) # Ajusta el eje Y más alto porque el Plan B sube hasta 3550
                plt.xlabel("Horas de Trabajo")
                plt.ylabel("Costo Total ($)")
                plt.title("Evolución de Costos - Plan B")
                plt.grid(True, linestyle="--")
                plt.legend()
                plt.show() #Muestra la funcion 
                print("Grafico generado con exito.")
            elif opcion == 2:
                print("Saliendo del programa... ¡Hasta luego!")
            else:
                print("Ingrese solo un numero correspondiente a una opcion.")


    #PLAN LINEAL C
    elif plan == 3:
        a= -2
        bCuadratica= 80
        c= 100

        vx = -bCuadratica / (2 * a)
        vy = a * (vx**2) + bCuadratica * vx + c
        discriminante = bCuadratica**2 - 4 * a * c
        raizC = discriminante**0.5
        limitesX = (-bCuadratica - raizC) / (2 * a) #segunda raiz 

        horas= int(input(f"Ingrese la cantidad de horas de uso del plan C (de 0 a {limitesX:.2f}): ")) #El ".2f" permite mostrar solo 2 decimales despues del punto.
        
        if horas < 0 or horas > limitesX:
            print(f"Error: Para evitar costos negativos, las horas deben estar entre 0 y {limitesX:.2f}.")
        else:
            costoTotal= a * (horas**2) + bCuadratica * horas + c
            CostoHora= a * (horas**2) + bCuadratica * horas

            print("--------------------------------------------------------")
            print("PRESUPUESTO PERSONALIZADO:")
            print(f"Para un uso de {horas} horas, el costo total del plan es de: ${costoTotal}")
            print("Detalles:")
            print(f"- Costo fijo inicial: ${c}")
            print(f"- Precio por hora de servicio: ${bCuadratica}")
            print(f"- Horas utilizadas: {horas}")
            print(f"- Costo por hora: ${CostoHora}")
            print("Informacion adicional:")
            print(f"- Punto maximo de costo: ${vy} a las {vx} horas")



        #SEGUNDO MENU C
        opcion = 0
        while opcion != 2:
            print("--------------------------------------------------------")
            opcion = int(input("Elija cómo desea continuar\n"
                                "1- Generar gráfico de este plan\n"
                                "2- Salir del programa\n"
                                "Opcion seleccionada: "))

            if opcion == 1: 
                print("Generando grafico...")
                x = np.linspace(0, limitesX, 100)
                y = a * (x**2) + bCuadratica * x + c

                plt.plot(x, y, label="Función Cuadrática (Plan C)", color="green")
                plt.plot(vx, vy, 'go', label=f"Vértice ({vx:.2f}, {vy:.2f})") 
                plt.plot(horas, costoTotal, 'ro', label=f"Tu Consumo (${costoTotal})")
                plt.xlim(0, limitesX)
                plt.ylim(0, vy +50) 
                plt.xlabel("Horas de Trabajo")
                plt.ylabel("Costo Total ($)")
                plt.legend()
                plt.grid(True, linestyle="--")
                plt.show()
                print("Grafico generado con exito.")

            elif opcion == 2:
                print("Saliendo del programa... ¡Hasta luego!")
            else:
                print("Ingrese solo un numero correspondiente a una opcion.")
    else:
        print("Ingrese solo un numero correspondiente a una opcion.")

except ValueError:
    print("Ingrese solo valores validos.")