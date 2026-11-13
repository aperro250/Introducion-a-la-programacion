# ---------------------------------------------------------------
# Iniciación a la programación en Python · Unidad 3 · Bloque S07
# Taller de errores: auditoría de cambios en la configuración
#
# Este programa tiene 10 errores: 3 de sintaxis, 3 de ejecución y
# 4 de lógica. Corrige uno, ejecuta y mira qué dice Python. Cuando
# el programa arranque, pruébalo con estos tres casos:
#   a) escribir 'fin' sin registrar ningún cambio
#   b) un cambio de 30 minutos exactos
#   c) escribir el cambio en mayúsculas
# ---------------------------------------------------------------

# --- CONSTANTES ---
CENTINELA = "fin"
MINUTOS_URGENTE = 30

# --- CABECERA ---
print("=" * 52)
print("   AUDITORÍA DE CAMBIOS EN LA CONFIGURACIÓN")
print("=" * 52)
print()
print(f"Escribe cada cambio realizado. Escribe '{CENTINELA}' para terminar.")
print()

# --- INICIALIZACIÓN ---
cambios = 0
urgentes = 0
listado = ""
minutos_totales = 0
i = 0

entrada = input("Cambio: ").strip()
# --- BUCLE DE CENTINELA ---
while entrada != CENTINELA and not entrada.isdigit() and not entrada == "0":
    entrada = input("Cambio: ").strip()

entrada = int(entrada)
while i < entrada:
    if entrada == CENTINELA:
        break
    texto = input("Minutos empleados: ").strip()
    while not texto.isdigit():
        print("[ERROR] Los minutos se escriben con cifras, sin decimales")
        texto = input("Minutos empleados: ").strip()
    minutos = int(texto)

    minutos_totales += minutos
    listado += entrada + " "

    if minutos > MINUTOS_URGENTE:
        urgentes += 1
        print(f"[AVISO] Ha durado {minutos} minutos: se anota como urgente")

    print(f"[OK] Cambio {cambios} registrado")
    cambios += 1
    print()

try:
    media_minutos = int(f"{minutos_totales / cambios:.1f}")
except ZeroDivisionError:
    media_minutos = 0

try:
    porcentaje = urgentes * 100 / cambios
except ZeroDivisionError:
    porcentaje = 0

# --- SALIDA ---
print()
print("-" * 52)
print(f"Cambios registrados: {cambios}")
print(f"Tiempo total: {minutos_totales} minutos")
if cambios == 0:
    print("[AVISO] No se ha registrado ningún cambio")
else:
    print(f"Urgentes (desde {MINUTOS_URGENTE} minutos): {urgentes}")
    print(f"Proporción de urgentes: {porcentaje:.1f} %")
    print(f"Media por cambio: {media_minutos} minutos")
    print(f"Listado: {listado}")

print()
print("Fin de la auditoría")
