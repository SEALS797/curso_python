num1=int(input("Introduce un número ganador:"))
num2=int(input("Introduce un número ganador:"))
num3=int(input("Introduce un número ganador:"))

win = [num1, num2, num3]
win.sort()
print("Los números ganadores son",win[0:3])
