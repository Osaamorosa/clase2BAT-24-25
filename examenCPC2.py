'''
Claudia Pujalte Calderón   5/2/25
Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. Si introducimos otro número nos da un error
'''

#solicitamos al usuario que nos de un número
n = int(input("dame un número del 1 al 7 para saber el día de la semana: "))

#verificar el número introducido y mostrar el día correspondiente ç
if n == 1 : 
    print("el día correspondiente es el lunes")
elif n== 2 : 
    print("el día correspondiente es el martes")
elif n== 3 : 
    print("el día correspondiente es el miércoles")
elif n== 4 : 
    print("el día correspondiente es el jueves")
elif n== 5 : 
    print("el día correspondiente es el viernes")
elif n== 6 : 
    print("el día correspondiente es el sábado")
elif n== 7 : 
    print("el día correspondiente es el domingo") 
else: 
    print("ERROR, el número introducido no es válido pues debe ser un número del 1 al 7")
