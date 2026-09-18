## Program information
'''
Author: Timoteo Brovenko
Class: 2-SMR-B
Date: 18/9/26
Version: 1.1.1
'''

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
line_mark = "======================================================="

# Variables de informacion del sistema
version = "3.0.1"
OS_name = "TeleviosionOS"

# Variables para emitar checkeo de Hardware

CPU = True
RAM = True
Disk = True
Ethernet = False
Mouse_Optical = False


# Metodo de checkeo de hardaware

def is_hardware_ok (is_hardware_working):
    if is_hardware_working == True:
        return "OK"
    else:
        return "ERROR"

# Imprimido de informacion

print (line_mark)

print (logo)
print ()
print ("\tSistema Operativo: " + OS_name)
print ("\tVersion: " + version)

print (line_mark)

print ()
print ("Comprobando hardware...")
print ()
print ("CPU: " f"[ {is_hardware_ok(CPU)} ]")
print ("RAM: " f"[ {is_hardware_ok(RAM)} ]")
print ("Disk: " f"[ {is_hardware_ok(Disk)} ]")
print ("Ethernet: " f"[ {is_hardware_ok(Ethernet)} ]")
print ("Optical mouse: " f"[ {is_hardware_ok(Mouse_Optical)} ]")
print ()

print (line_mark)

print (welcome_message)

print (line_mark)




