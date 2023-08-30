pan=int(input("Introduce el número de barras vendidas que no son frescas:"))
coste = 3.49
descuento = 0.6

resultado = pan*coste*(1-descuento)

print("El coste de una barra fresca es ₡"+ str(coste))
print("El descuento sobre una barra no fresca es " + str(descuento*100) + "%")
print("El coste final a pagar es ₡" + str(round(resultado,2)))


