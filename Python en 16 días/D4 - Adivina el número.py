from random import *

#Consultar por nombre y qué usuario adivine el número entre el 1-100 y posee 8 intentos para adivinarlo. Posee 4 Criterios

#Si el N es < a 1 o > 100 = N° no permitido
#si el N de usuario elige un N menor al que indica el programa, este dirá que número es mayor al elegido.
#si el N de usuario elige un N mayor al que indica el programa, este dirá que número es menor al elegido.
#si el usuario acierta se le informa que ha ganado y en cuantos intentos.

nombreUsuario = input("Ingresa tu nombre: ")

respuestasUsuario = []

for i in range(8):
    respuestasUsuario.append(input("Ingresa tu respuesta: "))
    if respuestasUsuario == randint(0, 101):
        print("¡Has ganado! En tan solo ")

