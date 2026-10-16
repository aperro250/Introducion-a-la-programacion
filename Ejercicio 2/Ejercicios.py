## Program information
"""
Author: Timoteo Brovenko
Class: 2-SMR-B
Date: 30/9/26
Version: 1.1.1
"""

def imprimir_nomre_ejercicio (numero):
    print ("\n"+"="*3 + f" Ejercicio {numero} " + "="*3 + "\n")

def waint_until_enter ():
    input("Precione enter")


imprimir_nomre_ejercicio (2.1)

RAM = 16
DISK = 512
PW_ON = True
name= "PC-AULA-14"
print ("="*3 + f" {name} " + "="*3)
print (f"RAM: {RAM:>5}" " GB")
print (f"DISK: {DISK:>5}" " GB")

waint_until_enter()
imprimir_nomre_ejercicio (2.2)

a = 5
b = a
a = 10
print(a, b)

waint_until_enter()
imprimir_nomre_ejercicio (2.3)

x = 3
y = 8
temp = 0

temp = x
x = y
y = temp

print(f"x={x}, y={y}")

x = 3
y = 8
x, y = y, x

print(f"x={x}, y={y}")

waint_until_enter()
imprimir_nomre_ejercicio (2.4)

Disc_total = 512
Disc_used = 187

print(f"Uso de disco: {(Disc_used/Disc_total)*100:.1f}%" )

waint_until_enter()
imprimir_nomre_ejercicio (2.5)

nombre = "PC-01"
ram_gb = 16
precio = 2.5
print("Total: " + "100")

waint_until_enter()
imprimir_nomre_ejercicio (2.6)

motherboard = 129.95
CPU = 189.00
RAM_16gb = 64.59

print (f"{'COMPONENTE':<15} {"PRECIO":>15}")
print (f"{'Placa base':<15} {motherboard:>15}")
print (f"{'CPU':<15} {CPU:>15}")
print (f"{'RAM 16':<15} {RAM_16gb:>15}")


