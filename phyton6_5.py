#Realiza un programa que lea dos números por teclado y permita elegir entre
#4 opciones en un menú
#1 - Mostrar la suma de los dos números
#2 - Mostrar la resta de los dos números (el primero menos el segundo)
#3 - Mostrar la multiplicación de los dos números
#4 - Salir del programa
#En caso de introducir una opción inválida, el programa volverá a solicitar otra
#opción hasta que el usuario elija salir.


print("porfavor, a continuación voy a pedirle que introduzca dos números")
n1 = int(input("dame el primer número: "))
n2 = int(input("dame el segundo número: "))

print("  ")
print("eliga que opción desea: ")
print("  ")
print("1. mostrar la suma de los dos números")
print("2. mostrar la resta de los dos números")
print("3. mostrar la multiplicación de los dos números")
print("4. salir del programa")
n3 = int(input("número de menu: "))

while n3 != 4 : 
    if n3 == 1 :
        print("la suma de los números es: ", n1+n2 )
    elif n3 == 2 : 
        print("la resta de los números es: ", n1-n2 )
    elif n3 == 3 : 
        print("la multiplicación de los números es: ", n1*n2 )
    else : 
        print("incorrecto")
    print("  ")
    print("eliga que opción desea: ")
    print("  ")
    print("1. mostrar la suma de los dos números")
    print("2. mostrar la resta de los dos números")
    print("3. mostrar la multiplicación de los dos números")
    print("4. salir del programa")
    n3 = int(input("número de menu: "))

print("  ")
print("salir del programa")


 

