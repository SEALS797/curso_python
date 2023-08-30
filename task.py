product_name = str(input("Introduce el nombre del producto:"))
precio = float(input("Introduce el precio unitario:"))
unidades = float(input("Introduce el número de unidades:"))
print(product_name+":",round(unidades,1),"unidades x",round(precio,1),"=",round(unidades*precio,1))