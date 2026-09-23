Importando biblioteca time para hacer uso de paracion de programa
Importando biblioteca random para poder hacer uso de valores aleatorios

Primero se ponen valores a variables que en el futuro seran imprimidas. Facilez de manejar informacion.

Se crean 2 metodos:

    is_hardware_ok: Hecho para ROOT-1 y ROOT-2
        Recive un valor boolean y comprube si es verdadero o falso, y segun la respuesta, imprime un [OK] o un [ERROR] segun el valor.
        El texto esta colorizado con codigos segun el tipo de mensage.
        Antes de enviar el estado,, el programa se para para un valor aleatorio entre 0,1-1,5 segundos.

    printtimer: Hecho para ROOT-3
        Recive un valor que despues para minimizar fallos es convertido a String.
        Crea un lista en la cual cada valor es un caracter de la String importada.
        Se entra en un ciclo for en el cual se imprime una letra a trabez de incrementando cada la x para poder seguir el orden de imprimo cada intracion la siguinente letra de la lista. Cada iteracion se para para un numero aleatorio entre 0-0.1 segundos
        Se sale de bucle para imprimir la ultima letra y hacer un salto de linea

Al llegar a la parte de imprimicion de texto, se utiliza:
    print para imprimir el logo y saltos de linea,
    printtimer para imprimir de letra en letra. En comprobacion de Hardware se usa:
        is_hardware_ok para hacer el texto en color y imitar una comprobacion de hardware.

nesecitad de investigar:

He tenido que  investigar los codigos de colores, el nobre de biblioteca para hacer un timer y biblioteca para randomizar (no era nesesario, pero he querido randomizar.).
Aprendido:

El metodo print() tiene paramentro end="" que permite customizar el final de la linea a imprimir. Por defecto es un salto de linea. Si se escribe un valor en blanco, no habra un salto de linea.
Fuentes:

ChatGPT para explicacion de funcionamiento de metodos para actividades ROOT
LISTA DE CODIGOS DE COLORES: https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
