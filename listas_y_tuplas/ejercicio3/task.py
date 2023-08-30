cursos = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
notas=[]
for i in cursos:
 notas.append(input(f"¿Qué nota has sacado en {i}?"))
for i in range(len(cursos)):
 print(f"En {cursos[i]} has sacado {notas[i]}")