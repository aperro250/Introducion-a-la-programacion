## Program information
'''
Author: Timoteo Brovenko
Class: 2-SMR-B
Date: 18/9/26
Version: 1.1.1
'''

import time
import random

# Logo del SO
logo = """
  _       _            _     _             
 | |_ ___| | _____   _(_)___(_) ___  _ __  
 | __/ _ \\ |/ _ \\ \\ / / / __| |/ _ \\| '_ \\ 
 | ||  __/ |  __/\\ V /| \\__ \\ | (_) | | | |
  \\__\\___|_|\\___| \\_/ |_|___/_|\\___/|_| |_|
"""

# Variables de visualisacion
welcome_message = "Bienvenido al Sistema!"
line_mark = "=" * 60

# Variables de informacion del sistema
version = "3.0.1"
OS_name = "TeleviosionOS"

# Variables para emitar checkeo de Hardware

CPU = True
RAM = True
Disk = True
Ethernet = False
Mouse_Optical = False

#------------------Metodos--------------------------------------------
# Metodo de checkeo de hardaware

def is_hardware_ok (is_hardware_working):
    time.sleep(random.uniform(0.1,1.5))
    if is_hardware_working == True:
        return "\033[96m[OK]\033[0m"
    else:
        return "\033[93m[ERROR]\033[0m"

def printtimer (text):
    text = str(text)
    character_list = list(text)
    list_length = len(character_list)
    for x in range(list_length-1):
        print(character_list[x], end="")
        time.sleep(random.uniform(0.0,0.1))
    print(character_list[list_length-1])
#-----------------------------------------------------------------------------------------
# Imprimido de informacion

print (line_mark)

print (logo)
print ("\n")
printtimer ("\tSistema Operativo: " + OS_name)
printtimer ("\tVersion: " + version)

print (line_mark)

print ()
printtimer ("Comprobando hardware...")
print ()
printtimer ("CPU: " + is_hardware_ok(CPU))
printtimer ("RAM: "  +is_hardware_ok(RAM))
printtimer ("Disk: "  +is_hardware_ok(Disk))
printtimer ("Ethernet: "  +is_hardware_ok(Ethernet))
printtimer ("Optical mouse: "  +is_hardware_ok(Mouse_Optical))
print ()

print (line_mark)

printtimer (welcome_message)

print (line_mark)




