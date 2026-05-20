M = [
    [120, 150, 100],
    [200, 180, 220],
    [90, 110, 95]
]

print("Promedio por función: ")

for fila in range(3):

    suma = 0

    for columna in range(3):
        suma += M[fila][columna]

    promedio = suma / 3

    print("Funcion", fila + 1, "=", promedio, "milisegundos")


print("Promedio por servidor: ")

for columna in range(3):

    suma = 0

    for fila in range(3):
        suma += M[fila][columna]

    promedio = suma / 3

    print("Funcion", columna + 1, "=", promedio, "milisegundos")

print()
print("MATRIZ TRANSPUESTA")

MT = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for fila in range(3):
    for columna in range(3):

        MT[columna][fila] = M[fila][columna]

for fila in range(3):
    print(MT[fila])