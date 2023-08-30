vocales = ["a","e","i","o","u"]

palabra = input("Introduce una palabra:")

for i in vocales:
    print("La vocal", i ,"aparece",palabra.count(i),"veces")