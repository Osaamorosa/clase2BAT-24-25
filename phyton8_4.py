#Crea un programa que pida al usuario 15 números enteros y luego muestre
#los que eran pares, todos ellos en la misma línea separados por un espacio en
#blanco.

datos = []

for i in range (15) :
    datos.append(int(input("dame un número entero: ")))

for i in range (15) : 
    if ((datos[i]) % 2) == 0 :
        print((datos[i]), end = " ")


