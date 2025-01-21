#Escribe un programa que pida un año y que escriba si es bisiesto o no.
#Se recuerda que los años bisiestos son múltiplos de 4, pero los múltiplos de 100
#no lo son, aunque los múltiplos de 400 sí

año = int(input("dame un año y dime si es bisiesto o no: "))

if año%4 == 0 or año%400 == 0 :
    print("es bisiesto")
elif año%100 != 0 : 
    print("no es bisiesto")
