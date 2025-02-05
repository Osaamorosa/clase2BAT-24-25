#Claudia Pujalte Calderón     5/2/25 
#Escribe un programa que pida números hasta que se introduzca un cero. Debe imprimir la suma de todos los números introducidos.

#iniciamos la suma en 0 
suma = 0
n = int(input("introduce un número (0 si desea finalizar): "))

#bucle que pide al usuario números hasta que ponga 0 
while n != 0 : 
    suma += n #sumamos los números 
    n = int(input("introduce otro número (0 si desea acabar: )")) #seguimos pidiendo números hasta que ponga 0 

#imprimimos la suma
print("la suma de los todos los números dados es: ", suma)

