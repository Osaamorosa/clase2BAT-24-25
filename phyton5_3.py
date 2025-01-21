#Escribe un programa que pida un año y que escriba si es bisiesto o no.
#Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100
#no lo son, aunque los múltiplos de 400 sí

año = int(input("Dame un año y dime si es bisiesto o no: "))

if (año%4 == 0 or año%400== 0 and año%100 != 0) : 
    print("Es bisiesto")
else : 
    print("No es bisiesto")
