# ---------------------------------------------------------------
# Misión: U02 - Control de acceso al laboratorio
# Alumno/a: Tymofii Brovenko
# Pareja: -
# Fecha: 30/10/26
# Nivel: Vía rápida / Nivel exigido / Nivel avanzado (borra los dos que no correspondan)
# Uso de IA: para buscar metodos y resolver problemas y fallo0s de sintaxis
# Referencias: codigo de importacion de json copiado y reescrito de mi anterior proyecto: https://github.com/aperro250/AlbionGDT-Stats
# ---------------------------------------------------------------

import json
# Importar time solo si coge el tiempo automaticamente del sistema
# import time

logo = '''\033[92m
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
   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀   \033[0m
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
    segundos = (givenTime % 3600) % 60

    return f"{horas}:{mins}:{segundos}"

def isTime (givenTime):
    try:
        horas = int(givenTime[:2])
        mins = int(givenTime[3:5])
        segundos = (int(givenTime[6:8]))

        if horas > 23:
            return False
        elif mins > 59:
            return False
        elif segundos > 59:
            return False

    except ValueError:
        return False

    return True
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

print(logo)
print("\t")
print("\033[91mBienvenido al sistema\033[0m")
print("\t")
while True:
    print('''\033[94m
    Elija lo que quiere hacer:
    
    (1) Validar la entrada del usuario
    (2) Cambiar o introducir registros de entrada
    (3) Consultar registros de entrada
    (4) Salir \t \033[0m
    ''')

    opcion = input("\033[93mOpcion: \033[0m")

    if opcion == "1":

        clear()

        while True:

            user = input("Usuario: ").lower()

            if len(user) < 3:
                print("Error, el usuario no puede ser menor de 3 caractres, intentalo de nuevo")
            else:
                break

        password = input("Contraseña: ")

        # Coger el tiempo del sistema de ahora
        #time_now = time.strftime("%H:%M:%S", time.localtime())

        while True:
            time_now = input("Introdusca elo tiempo: ")

            if isTime(time_now):
                break
            else:
                print("Timepo eroneo, introdusca un valor valido en formato HH:MM:SS y intentalo de nuevo")


        #print(time_to_seconds(time_now))
        if check_password(user, password):
            if check_time_is_permited(user, time_to_seconds(time_now)):
                print(f"Entrada registrada correctamente a las {time_now}")
            else:
                print(f"Entrada restringida. Usted solo puede entrar desde {seconds_to_time(get_available_start_time(user))} hasta {seconds_to_time(get_available_end_time(user))}")
        else:
            print("Error de verificacion, intentalo de nuevo")

    elif opcion == "2":
        print("Esta funcion esta en trabajo")
    elif opcion == "3":
        print("Esta funcion esta en trabajo")
    elif opcion == "4":
        exit()


#print(time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()))
