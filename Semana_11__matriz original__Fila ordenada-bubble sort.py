
def bubble_sort(fila):
    n=len(fila)
    for i in range(n-1):
        for j in range(n-1-1):
            if fila [j]> fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]

def mostrar_matriz(matriz_d2):            
    for fila in matriz_d2:
       print(fila)


matriz_d2 = [
    [20, 40, 25],
    [110, 99 , 155 ],
    [17, 16, 15]
]

print("Matriz original:")
for fila in matriz_d2:
    print(fila)

for fila in matriz_d2:
    bubble_sort(fila)

print("Fila ordenada_bubble sort")
mostrar_matriz(matriz_d2)



