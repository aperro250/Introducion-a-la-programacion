


# Variables
APERTURA = 8
CIERRE = 20
LIMITE_ALUMNADO = 14
APERTURA_VISITA = 10
CIERRE_VISITA = 13

APERTURA_MINUTOS = 8 * 60
CIERRE_MINUTOS = 20 * 60
LIMITE_ALUMNADO_MINUTOS = 14 * 60
APERTURA_VISITA_MINUTOS = 10 * 60
CIERRE_VISITA_MINUTOS = 13 * 60

ERROR_MESSAGE = "\033[91m[ERROR]\033[0m"
logo = '''\033[92m
==============================================
CONTROL DE ACCESO AL LABORATORIO
==============================================\033[0m'''
acompanante = ""
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
    elif len(usuario) < 3:
        print(f"{ERROR_MESSAGE} El usuario debe tener 3 o mas simbolos")
        errores += 1

    return errores

#============== COMPROVACIONES PERFIL ===================
acompanante =""
perfil = input("Perfil (alumnado/profesorado/tecnico/visita): ").strip().lower()
if perfil == "visita":
    acompanante = input("Introdusca nombre de la persona acompañante: ")
def check_perfil():

    # comprovar que este elegido uno de tres posibles perfiles
    perfiles = ["alumnado", "profesorado", "tecnico", "visita"]
    errores = 0

    if not perfil in perfiles:
        print(f"{ERROR_MESSAGE} El perfil debe ser uno de los tres posibles")
        errores += 1
    if perfil == "visita":
        if acompanante == "":
            print(f"{ERROR_MESSAGE} Usted debe tener una persona acompañante")
            errores += 1
    return errores
# ================ COMPROVACION DE TIEMPO ===================
centinela = -1
while True:
    tiempo = input("Hora (HH:MM): ")

    try:
        hora = tiempo.split(":")[0]
        minut = tiempo.split(":")[1]
        centinela = 0
    except:
        print("Hora incorecta, por vafor indicala en formato HH:MM")
    if centinela != -1:
        break

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

if perfil == "visita":
    print (f"{"Acompañante:":<15} {acompanante:<15}")

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
# Convertir el tiempo a minutos para facilidad en comprovacion
time = horas * 60 + minutos

acceso_corecto = "\t\033[38;5;46mAcceso corecto\033[0m"

if perfil == "alumnado":
    if APERTURA_MINUTOS <= time <= LIMITE_ALUMNADO_MINUTOS:
        print(acceso_corecto)
    else:
        print(f'''
\033[38;5;208m[DENEGADO]\033[0m Acceso denegado: fuera del horario de su perfil
Horario del laboratorio: de {APERTURA}:00 a {CIERRE}:00
El alumnado entra hasta las {LIMITE_ALUMNADO}:00
''')
elif perfil == "profesorado":
    if APERTURA_MINUTOS <= time <= CIERRE_MINUTOS:
        print(acceso_corecto)
    else:
        print(f'''
\033[38;5;208m[DENEGADO]\033[0m Acceso denegado: fuera del horario de su perfil
Horario del laboratorio: de {APERTURA}:00 a {CIERRE}:00
''')
elif perfil == "visita":
    if APERTURA_VISITA_MINUTOS <= time <= CIERRE_VISITA_MINUTOS:
        print(acceso_corecto)
    else:
        print(f'''
\033[38;5;208m[DENEGADO]\033[0m Acceso denegado: fuera del horario de su perfil
Horario del visita: de {APERTURA_VISITA}:00 a {CIERRE_VISITA}:00
''')
elif perfil == "tecnico":
    print(acceso_corecto)
else:
    print("Error interno de perfil")


