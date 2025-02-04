#Crea un programa que pida al usuario 12 números enteros, los guarde en un
#array y luego le pregunte de forma repetitiva qué número quiere buscar. Le
#responderá si dicho número estaba o no entre los datos que se habían
#introducido inicialmente. Dejará de repetirse cuando se introduzca el número 0.

datos = []

print("introduce 12 números enteros: ")
for i in range (12) : 
    n = int(input("número " + str (i + 1)  + ": "))
    datos.append(n)

busqueda = 10 

for _ in range(busqueda) : 
    buscar = int(input("¿qué número quieres buscar? (pulse 0 para salir del programa)"))

    if buscar == 0 : 
        print("programa finalizado")
        break

    if buscar in datos : 
        print("el número ", buscar, "está en la lista")
    else: 
        print("el número ", buscar, "el número no está en la lista")
