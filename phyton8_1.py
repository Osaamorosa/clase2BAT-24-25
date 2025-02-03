#8.1 Crea un array con los número 10, 20, 30, 40 y 50 y luego muestra los que hay
#en las posiciones impares (primero, tercero y quinto: 10, 30 y 50)

 
datos = [10, 20, 30, 40, 50] #DEFINIMOS ARRAY:

#FILTRAMOS Y MOSTRAMOS LAS POSICIONES IMPARES: 
impares = [datos[i] for i in range(len(datos)) if i % 2 == 0] 
print(impares)
