#7.1 Crea un programa que pida al usuario que introduzca su nombre y un
#número entero y escriba su nombre en pantalla tantas veces como indique ese
#número entero.

n = input("escriba su nombre: ")
n1 = int(input("introduzca un número entero: "))

for n in range(1,n1+1) :
    print(n)

