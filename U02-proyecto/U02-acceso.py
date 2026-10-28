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


def time_to_seconds(givenTime):
    # Take 2 first letters for hour, 2 before simbol for minutes and 2 more before simbol for seconds, example HH:MM:SS
    horas = int(givenTime[:2])
    mins = int(givenTime[3:5])
    segundos = int(givenTime[6:8])

    tiempo = (horas * 3600 ) + (mins * 60) + segundos

    return tiempo

def seconds_to_time(givenTime):
    horas = givenTime // 3600
    mins = (givenTime % 3600) // 60
    segundos = givenTime % 60
    segundos = givenTime - (mins * 60)

    return f"{horas}:{mins}:{segundos}"

def clear():
    print("\033[H\033[J", end="")

def check_password(user, password):
    with open("usuarios.json", "r") as file:
        users = json.load(file)
    if user in users:
        if users[user]["password"] == password:
            return True
        else:
            return False
    return False

def check_permission(user, permission):
    with open("usuarios.json", "r") as file:
        users = json.load(file)
        if permission in user[user]["permissions"]:
            return True
        else:
            return False

def  check_time_is_permited(user, time):
    with open("usuarios.json", "r") as file:
        users = json.load(file)
    with open("perfiles.json", "r") as file:
        perfiles = json.load(file)
    user_permision = users[user]["permission"]

    if perfiles[user_permision]["tiempo_permitido"]["start"] <= time <= perfiles[user_permision]["tiempo_permitido"]["end"]:
        return True
    else:
        return False

def get_available_start_time(user):
    with open("usuarios.json", "r") as file:
        users = json.load(file)
    with open("perfiles.json", "r") as file:
        perfiles = json.load(file)
    perfil = users[user]["permission"]

    return perfiles[perfil]["tiempo_permitido"]["start"]


def get_available_end_time(user):
    with open("usuarios.json", "r") as file:
        users = json.load(file)
    with open("perfiles.json", "r") as file:
        perfiles = json.load(file)
    perfil = users[user]["permission"]

    return perfiles[perfil]["tiempo_permitido"]["end"]
# ---------------- Start program ---------------------

print(seconds_to_time(2234))
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

    opcion = input("Opcion: ")

    if opcion == "1":

        clear()
        user = input("Usuario: ")
        password = input("Contraseña: ")

        #time_now = time.strftime("%H:%M:%S", time.localtime())
        time_now = "20:00:00"

        #print(time_to_seconds(time_now))
        if check_password(user, password):
            if check_time_is_permited(user, time_to_seconds(time_now)):
                print(f"Entrada registrada correctamente a las {time_now}")
            else:
                print(f"Entrada restringida. Usted solo puede entrar desde {seconds_to_time(get_available_start_time(user))} hasta {seconds_to_time(get_available_end_time(user))}")
        else:
            print("Error, intentalo de nuevo")



#print(time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()))
