# ---------------------------------------------------------------
# Misión: U02 - Control de acceso al laboratorio
# Alumno/a: Tymofii Brovenko
# Pareja: -
# Fecha: 30/10/26
# Nivel: Nivel avanzado
# Uso de IA: para buscar metodos y resolver problemas y fallos de sintaxis. Puede visualizar las preguntas en https://chatgpt.com/share/6aed959c-d998-83eb-a646-ef3a3f3bfb2c
# ---------------------------------------------------------------

# Variables
APERTURA = 8
CIERRE = 20
LIMITE_ALUMNADO = 14
APERTURA_VISITA = 10
CIERRE_VISITA = 13

APERTURA_MINUTOS = APERTURA * 60
CIERRE_MINUTOS = CIERRE * 60
LIMITE_ALUMNADO_MINUTOS = LIMITE_ALUMNADO * 60
APERTURA_VISITA_MINUTOS = APERTURA_VISITA * 60
CIERRE_VISITA_MINUTOS = CIERRE_VISITA * 60

ERROR_MESSAGE = "\033[91m[ERROR]\033[0m"
logo = '''\033[92m
==============================================
CONTROL DE ACCESO AL LABORATORIO
==============================================\033[0m'''
acompanante = ""
# pedir el perfil y la hora igual que el usuario

# Inicio programa

print (logo + "\n")
#============ COMPROBACIONES USUARIO ===================

usuario = input("\033[33mUsuario: \033[0m").strip().lower()

def check_user():

    errores = 0
    # validar que usuario no es vicio
    if usuario == "":
        print(f"{ERROR_MESSAGE} El usuario no puede estar vacío")
        errores += 1

    # validar la longitud del usuario, el perfil y la hora
    elif len(usuario) < 3:
        print(f"{ERROR_MESSAGE} El usuario debe tener 3 o mas símbolos")
        errores += 1

    return errores

#============== COMPROBACIONES PERFIL ===================
perfil = input("\033[33mPerfil \033[91m(alumnado/profesorado/tecnico/visita)\033[33m: \033[0m").strip().lower()
if perfil == "visita":
    acompanante = input("\033[33mIntroduzca nombre de la persona acompañante: \033[om").strip().lower()
def check_perfil():

    # comprobar que este elegido uno de tres posibles perfiles
    perfiles = ["alumnado", "profesorado", "técnico", "visita"]
    errores = 0

    if not perfil in perfiles:
        print(f"{ERROR_MESSAGE} El perfil debe ser uno de los posibles")
        errores += 1
    elif perfil == "visita":
        if acompanante == "":
            print(f"{ERROR_MESSAGE} Usted debe tener una persona acompañante")
            errores += 1
    return errores
# ================ COMPROBACIÓN DE TIEMPO ===================
centinela = -1
while True:
    tiempo = input("\033[33mHora \033[91m(HH:MM)\033[33m: \033[0m")

    try:
        hora = tiempo.split(":")[0]
        minut = tiempo.split(":")[1]
        centinela = 0
    except:
        print("Hora incorrecta, por favor indicala en formato HH:MM")
    if centinela != -1:
        break

horas = -1
minutos = -1

def check_time():
    global horas, minutos
    errores = 0
# Comprobación para horas
    if hora.isdigit():
        if 0 <= int(hora) <= 23:
            horas = hora
        else:
            print(f"{ERROR_MESSAGE} la hora debe ser entre 0 y 23 horas")
            errores += 1
    else:
        print(f"{ERROR_MESSAGE} la hora debe ser un numero")
        errores += 1

# Comprobaciones para minutos
    if minut.isdigit():
        if 0 <= int(minut) <= 59:
            minutos = minut
        else:
            print(f"{ERROR_MESSAGE} los minutos deben ser entre 0 y 59 minutos")
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


# ============== PONER INFORMACIÓN ============

print (f"\033[34m{"Usuario:":<15} {usuario:<15}\033[0m")
print (f"\033[34m{"Perfil:":<15} {perfil:<15}\033[0m")

if perfil == "visita":
    print (f"\033[34m{"Acompañante:":<15} {acompanante:<15}\033[0m")

if horas != -1:
    if minutos != -1:
        print(f"\033[34m{"Horas:":<15} {f"{horas}:{minutos}":<15}\033[0m")
else:
    print("38;5;208m[DENEGADO] Error interno de centinela \033[0m")
    exit()



# =============== COMPROBAR HORA PERMITIDA =====================
#======================= ACCESO ===============================0

horas = int(horas)
minutos = int(minutos)
# Convertir el tiempo a minutos para facilidad en comprobación
time = horas * 60 + minutos

acceso_correcto = "\t\033[38;5;46mAcceso correcto\033[0m"
acceso_denegado = "\033[38;5;208m[DENEGADO]\033[0m"

if perfil == "alumnado":
    if APERTURA_MINUTOS <= time <= LIMITE_ALUMNADO_MINUTOS:
        print(acceso_correcto)
    else:
        print(f'''
{acceso_denegado} Acceso denegado: fuera del horario de su perfil
Horario del laboratorio: de \033[92m{APERTURA}:00\033[0m a \033[92m{CIERRE}:00\033[0m
El alumnado entra hasta las \033[92m{LIMITE_ALUMNADO}:00\033[0m
''')
elif perfil == "profesorado":
    if APERTURA_MINUTOS <= time <= CIERRE_MINUTOS:
        print(acceso_correcto)
    else:
        print(f'''
{acceso_denegado} Acceso denegado: fuera del horario de su perfil
Horario del laboratorio: de \033[92m{APERTURA}:00\033[0m a \033[92m{CIERRE}:00\033[0m
''')
elif perfil == "visita":
    if APERTURA_VISITA_MINUTOS <= time <= CIERRE_VISITA_MINUTOS:
        print(acceso_correcto)
    else:
        print(f'''
{acceso_denegado} Acceso denegado: fuera del horario de su perfil
Horario del visita: de \033[92m{APERTURA_VISITA}:00 a \033[92m{CIERRE_VISITA}:00\033[0m
''')
elif perfil == "técnico":
    print(acceso_correcto)
else:
    print("Error interno de perfil")


