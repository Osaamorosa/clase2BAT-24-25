#Pide al usuario 10 números y luego muestra los que son pares

datos = []

for i in range (10) :
    datos.append(int(input("dame 10 números: ")))

pares = []

for j in range(len(datos)) :
    if datos[j] % 2 == 0 :
        pares.append(datos[j])
print("los números pares son: ", pares)

