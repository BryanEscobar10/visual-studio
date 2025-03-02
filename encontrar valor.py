matriz_d2 = [
    [2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]
]
valor_buscado = 10

encontrado = False
posicion = None

for fila_index, fila in enumerate(matriz_d2):
    for columna_index, valor in enumerate(fila):
        if valor == valor_buscado:
            encontrado = True
            posicion = (fila_index, columna_index)
            break  
if encontrado:
    print(f"Se encontró el valor específico {valor_buscado} en la posición: {posicion}")
else:
    print(f"El valor especifico {valor_buscado} no se encontró en la matriz")
