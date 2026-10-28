## Program information
"""
Author: Timoteo Brovenko
Class: 2-SMR-B
Date: 16/10/26
Version: 1.1.1
"""

import json
import time

logo = '''
▄▄▄▄▄▄▄▄▄            ▄▄▄▄▄▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   
▄       ▓     ░    ▄▀            ▀▄  ▄              ▀▄ 
█       ▒   ·░░░  ▐▌              ▐▌ █               ▐▌
█       ░   ░▒▒░  ▓               ░█ ▓      ▒▀▀░     ░█
▓       █   ░░░   ▒      █▀▀▄      █ ▒      ░  ▒     ▐▌
░       █    ░ ·  ░      █▄▄▒    ┼┼█ ░      ▀▀▀▀    ▄▀ 
█ ┼     █       · █┼            ┼┼┼█ █┼┼    ▒▀▀▀▄   ▀▄ 
█┼┼┼   ┼█▄▄▄▄▄▄▄▄ █┼┼   ┼█▀▀█┼   ┼┼█ █┼┼┼┼ ┼▓   ░    ▐▌
█┼┼┼ ┼┼┼┼┼┼┼┼┼┼┼░ █┼┼┼┼┼┼░  █┼┼┼ ┼┼░ █┼┼┼┼┼┼▒   ▓┼┼ ┼┼░
▐▌┼┼┼┼┼┼┼┼┼┼┼┼┼┼▒ █┼┼┼┼┼┼▒  █┼┼┼┼┼┼▒ █┼┼┼┼┼┼░▄▄▄▀┼┼┼┼▐▌
·▀▄┼┼┼┼┼┼┼┼┼┼┼┼┼▓ █┼┼┼┼┼┼▓  █┼┼┼┼┼┼▓ █┼┼┼┼┼┼┼┼┼┼┼┼┼┼▄▀ 
   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀   
'''

# ------------------- Methods ------------------

def preguntar(text):
    return input(text)


def convert_time(givenTime):
    # Take 2 first letters for hour, 2 before simbol for minutes and 2 more before simbol for seconds, example HH:MM:SS
    horas = int(givenTime[:2])
    mins = int(givenTime[3:5])
    segundos = int(givenTime[6:8])

    tiempo = (horas * 3600 ) + (mins * 60) + segundos

    return tiempo

def clear():
    print("\033[H\033[J", end="")


# ---------------- Start program ---------------------

print(logo)
print("\t")
print("Bienvenido al sistema")
print("\t")
while True:
    print('''
    Elija lo que quiere hacer:
    
    (1) Validar la entrada del usuario
    (2) Cambiar o introducir registros de entrada
    (3) Consultar registros de entrada
    
    ''')

    opcion = preguntar("Opcion: ")

    if opcion == "1":
        clear()

        user = preguntar("Usuario: ")
        password = preguntar("Contraseña: ")


#print(time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()))
