from random import *

#Consultar por nombre y qué usuario adivine el número entre el 1-100 y posee 8 intentos para adivinarlo. Posee 4 Criterios

#Si el N es < a 1 o > 100 = N° no permitido
#si el N de usuario elige un N menor al que indica el programa, este dirá que número es mayor al elegido.
#si el N de usuario elige un N mayor al que indica el programa, este dirá que número es menor al elegido.
#si el usuario acierta se le informa que ha ganado y en cuantos intentos.

nombreUsuario = input("Ingresa tu nombre: ")
respuestasUsuario = []
numeroSecreto = randint(1,101)

print(numeroSecreto)

for intento in range(8):

    try:
        respuestasUsuario.append(int(input("Ingresa tu respuesta: ")))
        if respuestasUsuario[intento] < 1 or respuestasUsuario[intento] > 100:
            print(f"¡Mal ahí {nombreUsuario}! \nDebes ingresar un número entre el 1-100.\nQuedan: {intento} intentos.")
        elif respuestasUsuario[intento] == numeroSecreto:
            print(f"¡Has adivinado {nombreUsuario}! \nEl número secreto era: {numeroSecreto} y tan solo en {intento} intentos.")
            break
        elif respuestasUsuario[intento] > numeroSecreto:
            print(f"Equivocado {nombreUsuario}.\nEl número secreto es menor al elegido.\nQuedan: {intento} intentos.")
        elif respuestasUsuario[intento] < numeroSecreto:
            print(f"Equivocado {nombreUsuario}.\nEl número secreto es mayor al elegido.\nQuedan: {intento} intentos.")
    finally:
        pass



