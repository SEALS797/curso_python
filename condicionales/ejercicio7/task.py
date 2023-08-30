points = float(input("Introduce tu puntuación:"))

monto = 2400 * points

aceptable = 0.4
meritorio = 0.6
inaceptable = 0.0

if points == aceptable:
    print("Tu nivel de rendimiento es", aceptable)

elif points == meritorio:
    print("Tu nivel de rendimiento es",meritorio)

elif points == inaceptable:
    print("Tu nivel de rendimiento es",inaceptable)

else:
    print("Esta puntuación no es válida")

