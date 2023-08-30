invertir = int(input("¿Cantidad a invertir?"))
interes = int(input("¿Interés porcentual anual?"))
a = int(input("¿Años?"))
for i in range(1, a+1):
    invertir *= 1 + interes / 100
    print("Capital tras {} años: {}".format(i, round(invertir, 2)))