currency = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

divis = input("Introduce una divisa:")

if divis in currency:
    print(currency.get(divis))
else:
    print("La divisa no está.")