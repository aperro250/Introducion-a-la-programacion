# Variables
APERTURA = 8
CIERRE = 20
LIMITE_ALUMNADO = 14
ERROR_MESSAGE = "\033[91m[ERROR]\033[0m"
logo = '''\033[92m
==============================================
CONTROL DE ACCESO AL LABORATORIO
==============================================\033[0m'''

# pedir el perfil y la hora igual que el usuario

# Inicio programa

print (logo + "\n")
#============ COMPROVACIONES USUARIO ===================

usuario = input("Usuario: ").strip().lower()

def check_user():

    errores = 0
    # validar que usuario no es viacio
    if usuario == "":
        print(f"{ERROR_MESSAGE} El usuario no puede estar vacío")
        errores += 1

    # validar la longitud del usuario, el perfil y la hora
    if len(usuario) < 3:
        print(f"{ERROR_MESSAGE} El usuario debe tener 3 o mas simbolos")
        errores += 1

    return errores

#============== COMPROVACIONES PERFIL ===================

perfil = input("Perfil (alumnado/profesorado/tecnico): ")

def check_perfil():

    # comprovar que este elegido uno de tres posibles perfiles
    perfiles = ["alumnado", "profesorado", "tecnico"]
    errores = 0

    if not perfil in perfiles:
        print(f"{ERROR_MESSAGE} El perfil debe ser uno de los tres posibles")
        errores += 1
    return errores
# ================ COMPROVACION DE TIEMPO ===================

tiempo = input("Hora (HH:MM): ")
hora = tiempo.split(":")[0]
minut = tiempo.split(":")[1]
horas = -1
minutos = -1

def check_time():
    global horas, minut, horas, minutos
    errores = 0
# Comprovacion para horas
    if hora.isdigit():
        if 0 <= int(hora) <= 23:
            horas = hora
        else:
            print(f"{ERROR_MESSAGE} la hora debe ser entre 0 y 23 horas")
            errores += 1
    else:
        print(f"{ERROR_MESSAGE} la hora debe ser un numero")
        errores += 1

# Comprovaciones para minutos
    if minut.isdigit():
        if 0 <= int(minut) <= 59:
            minutos = minut
        else:
            print(f"{ERROR_MESSAGE} los minutos deben ser entre 0 y 60 minutos")
            errores += 1
    else:
        print(f"{ERROR_MESSAGE} los minutos deben ser un numero")
        errores += 1
    return errores

#================ CONTADOR DE ERRORES =================
print ("\n")
errores = check_user() + check_perfil() + check_time()

if errores > 0:
    print(f"\033[38;5;208m[DENEGADO]\033[0m {errores} dato(s) incorrecto(s)")
    exit()
else:
    pass # decidir el acceso y mostrar la ficha


# ============== PONER INFORMACION ============

print (f"{"Usuario:":<15} {usuario:<15}")
print (f"{"Perfil:":<15} {perfil:<15}")

if horas != -1:
    if minutos != -1:
        print(f"{"Horas:":<15} {f"{horas}:{minutos}":<15}")
else:
    print("Error interno de centinela")
    exit()



# =============== COMPROBAR HORA PERMITIDA =====================
#======================= ACCESO ===============================0

horas = int(horas)
minutos = int(minutos)

acceso_corecto = "\t\033[38;5;46mAcceso corecto\033[0m"

if perfil == "alumnado":
    if APERTURA <= horas <= LIMITE_ALUMNADO:
        print(acceso_corecto)
    else:
        print(f'''
\033[38;5;208m[DENEGADO]\033[0m Acceso denegado: fuera del horario de su perfil
Horario del laboratorio: de {APERTURA}:00 a {CIERRE}:00
El alumnado entra hasta las {LIMITE_ALUMNADO}:00
''')
elif perfil == "profesorado":
    if APERTURA <= horas <= CIERRE:
        print(acceso_corecto)
    else:
        print(f'''
\033[38;5;208m[DENEGADO]\033[0m Acceso denegado: fuera del horario de su perfil
Horario del laboratorio: de {APERTURA}:00 a {CIERRE}:00
''')
elif perfil == "tecnico":
    print(acceso_corecto)
else:
    print("Error interno de perfil")


