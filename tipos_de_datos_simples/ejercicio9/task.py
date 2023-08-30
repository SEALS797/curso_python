

inv=float(input("¿Cantidad a invertir?"))
int=float(input("¿Interés porcentual anual?"))
yrs=float(input("¿Años?"))

resultado= round(inv*(1+int / 100)**yrs,2)
print("Capital final:",resultado)


