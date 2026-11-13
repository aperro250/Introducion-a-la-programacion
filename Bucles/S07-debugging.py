# ---------------------------------------------------------------
# Iniciación a la programación en Python · Unidad 3 · Bloque S07
# Debugging: control de acceso al laboratorio
#
# Este programa tiene 9 errores: 3 de sintaxis, 3 de ejecución y
# 3 de lógica. Corrige uno, ejecuta y mira qué dice Python. Cuando
# arranque, pruébalo con estos tres casos:
#   a) escribir el usuario con mayúscula inicial: Admin
#   b) declarar 0 equipos para revisar
#   c) fallar la contraseña las tres veces
# ---------------------------------------------------------------

# --- CONSTANTES ---
USUARIO_VALIDO = "admin"
CLAVE_VALIDA = "root2026"
LIMITE_INTENTOS = 3
MINUTOS_BLOQUEO = 15

# --- Variables ---
acertada = False

# --- CABECERA ---
print("=" * 50)
print("   CONTROL DE ACCESO AL LABORATORIO")
print("=" * 50)
print()

# --- AUTENTICACIÓN: INTENTOS LIMITADOS CON BANDERA ---
intentos = 0

while intentos < LIMITE_INTENTOS and not acertada:
    usuario = input(f"Intento {intentos + 1} de {LIMITE_INTENTOS}. Usuario: ").strip().lower()
    clave = input("Contraseña: ").strip()

    if usuario == USUARIO_VALIDO and clave == CLAVE_VALIDA:
        acertada = True
        print("[OK] Credenciales correctas")
    else:
        intentos += 1
        print(f"[ERROR] Credenciales incorrectas. Intentos restantes: {LIMITE_INTENTOS - intentos}")
    print()

# --- REGISTRO DE LA REVISIÓN ---
if acertada:
    print("[ACCESO] Sesión iniciada")
    print()

    # El dato se pide hasta que es válido
    texto = input("Equipos que vas a revisar: ").strip()
    while not texto.isdigit():

        texto = input("Equipos que vas a revisar: ").strip()
    equipos = int(texto)

    revisados = 0
    minutos_totales = 0
    minutos_media = "0"
    if equipos != 0:
        while revisados < equipos:
            revisados += 1
            while True:
                try:
                    minutos_totales += int(input(f"Minutos empleados en el equipo {revisados}: "))
                    break
                except ValueError:
                    print("[ERROR] Escribe un número entero, sin signos ni decimales")

            minutos_media = float(f"{minutos_totales / revisados:.1f}")

    print()
    print("-" * 50)
    print(f"Equipos revisados: {revisados}")
    print(f"Tiempo total: {minutos_totales} minutos")
    print(f"Media por equipo: {minutos_media} minutos")
else:
    print(f"[AVISO] Cuenta bloqueada durante {MINUTOS_BLOQUEO} minutos")

print()
print("Fin del registro")
