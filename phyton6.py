"""
#programa que calcula la división entre dos números
dividendo = int(input("dividendo:"))
divisor = int(input("divisior: "))

while divisor == 0 :
    divisor = int(input("divisor que no sea 0: "))
print("el resultado de la división es", dividendo / divisor)

"""
#programa que calcula la suma de x números
suma = 0
n = float(input("dame un número: "))

while (n != 0) :
    suma = suma + n 
    n = float(input("dame otro número: "))
print("la suma es:", suma)

