#Pide al usuario su nombre y un número. Después de esto, muestra por
#pantalla, su nombre el número de veces que haya elegido. Comprueba y evita
#que se produzcan errores.

nombre = input("dime tu nombre: ")
n1 = int(input("dame un número: "))
n2 = n1

while (n1 != 0 ):
    n1 = (n1-1)
    print("este es tu nombre", nombre, "este es tu número", n1)