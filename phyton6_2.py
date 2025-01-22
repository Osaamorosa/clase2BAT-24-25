#Pide una clave y una contraseña al usuario. No se le dejará proseguir hasta
#que el código sea admin y la clave 0987. Debes utilizar conectores lógicos (and,
#or, not,...)

clave = input("dame un código que contenga 5 palabras: ")
contraseña = input("dame una clave con 4 números: ")

if (clave != "admin" or contraseña != "0987") : 
    print("código y contraseña NO válido")
else : 
    print("código y contraseña aceptado")

