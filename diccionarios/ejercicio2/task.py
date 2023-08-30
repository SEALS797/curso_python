inf = {}

inf.update({"nombre": input("¿Cómo te llamas?")})
inf.update({"edad": input("¿Cuántos años tienes?")})
inf.update({"direccion": input("¿Cuál es tu dirección?")})
inf.update({"telefono": input("¿Cuál es tu número de teléfono?")})


print(inf['nombre'],"tiene",inf["edad"],"años, vive en",inf["direccion"],"y su número de teléfono es",inf["telefono"])