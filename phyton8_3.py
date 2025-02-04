#Pide al usuario un número del 1 al 12 y escribe el número del mes
#correspondiente (1 = enero, 2= febrero,..) usando un array

meses = ["enero", "febrero", "marzo", "abirl", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

n = int(input("dame un número del 1 al 12: "))

if 1 <= n <= 12 : 
    print("el mes correspondiente al número dado es: ", meses[n - 1])

else: 
    print("número no válido, introduzca otra número entre el 1 y el 12: ")
