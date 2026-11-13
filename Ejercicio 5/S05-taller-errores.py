# ---------------------------------------------------------------
# Iniciación a la programación en Python · Unidad 2 · Bloque S05
# Taller: if-else con más errores
# Corrígelos uno a uno, ejecuta tras cada corrección.
# ---------------------------------------------------------------

print("=" * 50)
print("   VALIDACIÓN DE ENTRADA A CLASE")
print("=" * 50)
print()

# Constantes
HORA_ENTRADA_MIN = 9
HORA_ENTRADA_MAX = 10
RETRASO_MINIMO = 5

# Entrada de datos
nombre = input("Nombre del alumno: ").strip()
hora = int(input("Hora de entrada (formato 0-23): "))
retraso_min = int(input("Minutos de retraso (0 si llega a tiempo): "))
print()

# Validaciones
nombre_valido = len(nombre) > 3
hora_entrada = HORA_ENTRADA_MIN <= hora <= HORA_ENTRADA_MAX
retraso_valido = retraso_min < RETRASO_MINIMO

# Mostrar entrada
print(f"Alumno: {nombre}")
print(f"Hora: {hora}:00")
print(f"Retraso: {retraso_min} minutos")
print()

if nombre_valido:
    print("[OK] Nombre válido")
else:
    print("[ERROR] Nombre debe tener más de 3 caracteres")

asistencia = "presente"

if not hora_entrada:
    print("[PUNTUAL] Entrada dentro del horario")
else:
    print("[FUERA DE HORARIO] Entrada fuera del horario permitido")

if retraso_valido:
    print("[OK] Retraso aceptable")

if nombre_valido:
    if retraso_valido:
        print("[ACCESO] Puede entrar a clase")
        print("Registro completado")

print()
print("Fin de validación")
