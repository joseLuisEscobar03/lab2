# Programa para registrar datos de un paciente

# aqui es para solicitar información del paciente
print("**************BIENVENIDOS****************")
nombre = input("Ingrese el nombre del paciente: ")
edad = int(input("Ingrese la edad del paciente: "))
peso_lb = float(input("Ingrese el peso del paciente en libras (lb): "))
atendido = input("¿El paciente fue atendido anteriormente? (si/no): ").strip().lower()

# aqui para verificar si fue atendido
if atendido == "si":
    estado_atencion = "El paciente si fue atendido anteriormente."
elif atendido == "no":
    estado_atencion = "El paciente no fue atendido anteriormente."
else:
    estado_atencion = "Respuesta no válida."

# Mostrar la información ingresada
print("\nDatos del Paciente:")
print("-" * 30)
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Peso: {peso_lb} lb")
print(estado_atencion)
print("******************************")
