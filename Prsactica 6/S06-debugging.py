# ---------------------------------------------------------------
# Iniciación a la programación en Python · Unidad 2 · Bloque S06
# Debugging: elif
# Este programa clasifica tareas por duración. Búscalos, corrígelos.
# ---------------------------------------------------------------

print("=" * 50)
print("   CLASIFICACIÓN DE TAREAS POR DURACIÓN")
print("=" * 50)
print()

# Entrada
tarea = input("Nombre de la tarea: ").strip()
duracion = int(input("Duración estimada (minutos): "))
print()

# Mostrar datos
print(f"Tarea: {tarea}")
print(f"Duración: {duracion} minutos")
print()

if duracion < 15
    categoria = "Rápida"
    print("[RÁPIDA] Menos de 15 minutos")
elif duracion < 60:
    categoria = "Normal"
    print("[NORMAL] Entre 15 y 60 minutos")
elif duracion = 120:
    categoria = "Larga"
    print("[LARGA] Entre 60 y 120 minutos")
else
    categoria = "Muy larga"
    print("[MUY LARGA] Más de 120 minutos")

print()
print(f"Categoría: {categoria}")
print("Clasificación completada")
