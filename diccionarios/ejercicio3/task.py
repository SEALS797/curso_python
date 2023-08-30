frutas = {"Plátano":50, "Manzana":60, "Pera":70, "Naranja":80}
fruit = input("¿Qué fruta quieres?")
kilo = input("¿Cuántos kilos?")
if fruit in frutas:
    print(f"{frutas[fruit]} kilos de Platano valen{kilo*frutas[fruit]}")
else:
    print("Lo siento, la fruta Uva no está disponible.")