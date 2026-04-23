nombre = input("Ingrese su nombre: ")
carrera = input("Ingrese el nombre de su Carrera: ")
codasig = input("Ingrese el código de la asignatura: ")

print("===== Perfil del Estudiante =====")
print(f"Nombre:           {nombre.upper()}")
print(f"Concatenado:     {carrera[0]+codasig[-1]}")
print(f"Cantidad de letras:      {len(carrera)}")
