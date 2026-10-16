## Program information
"""
Author: Timoteo Brovenko
Class: 2-SMR-B
Date: 16/10/26
Version: 1.1.1
"""

Line = "-" * 40

def wait ():
    input("\nPrecione enter para continuar")
    print("\n" + Line)

# ------------Ejercicio 3.1-----------------------------------
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

vsuma = num1 + num2
vresta = num1 - num2
vmultiplicacion = num1 * num2
vdivicion = num1 / num2
vcociente = num1 // num2
vresto = num1 % num2

print(f"{num1} + {num2} = {vsuma}")
print(f"{num1} - {num2} = {vresta}")
print(f"{num1} * {num2} = {vmultiplicacion}")
print(f"{num1} / {num2} = {vdivicion}")
print(f"{num1} // {num2} = {vcociente}")
print(f"{num1} % {num2} = {vresto}")

# --------------------------------------------------------------
wait()
# --------------Ejercicio 3.2---------------------------------

mb = int(input("Dame la cantidad de MB: "))

gb = round(mb / 1024, 2)

print(f"{mb}MB son {gb}GB")

# --------------------------------------------------------------
wait()
# --------------Ejercicio 3.3---------------------------------

t_seconds = int(input("Dame la cantidad de tiempo: "))

hours = t_seconds // 3600
minutes = (t_seconds % 3600) // 60
seconds = (t_seconds % 3600) % 60

print(f"{hours}h {minutes}m {seconds}s")

# --------------------------------------------------------------
wait()
# --------------Ejercicio 3.4---------------------------------

# El error esta en que hay que convertir con int() la entrada que se intruduce en la asignacion de las variables despues del input
precio = int(input("Precio: "))
unidades = int(input("Unidades: "))
print("Total:", precio * unidades)

# --------------------------------------------------------------
wait()
# --------------Ejercicio 3.5---------------------------------

Year = 2026
anyo_nacimiento = int(input("Dame el año de nacimiento: "))

# La ñ no es un ASSCI simvolo, por lo que lo sustituyo por "ny"
anyos_actuales = Year - anyo_nacimiento

print (f"Este año cumple {anyos_actuales} años")


# --------------------------------------------------------------
wait()
# --------------Ejercicio 3.6---------------------------------

N_equipos_por_mesa = 3

n_equipos = int(input("Ingrese el numero de equipos: "))

mesas_llenas = n_equipos // N_equipos_por_mesa
r_equipos = n_equipos % N_equipos_por_mesa

print (f"Se llenaran {mesas_llenas} mesas y quedaran {r_equipos} equipos sueltos")

# --------------------------------------------------------------
wait()
# --------------Ejercicio 3.7---------------------------------

print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20
print(10 / 4) # 2.5
print(10 // 4) # 2
print(10 % 4) # 2
print(2 ** 3 ** 2) # 64
print(int(7.9)) # 7
print(round(7.9)) # 8