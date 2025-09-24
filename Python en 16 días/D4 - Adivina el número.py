from random import *

nombreUsuario = input("\nBienvenidos a 'ADIVINA EL NÚMERO SECRETO' en un rango de 1-100, ¿Podrás?.\nDe premio, te ganas senda patá en la raja.\nAhora, ingresa tu nombre para conocerte: ")


def nuevoJuego():
    numeroSecreto = randint(1, 101)
    respuestasUsuario = []
    acertado = False
    print(f"\nUn gusto {nombreUsuario}.\nCreando número...\nNúmero secreto creado, ¿Crees poder adivinarlo?")

    for intento in range(8):
        intentosRestantes = 8 - intento - 1

        try:
            respuestasUsuario.append(int(input("\nIngresa tu respuesta: ")))
            if respuestasUsuario[intento] < 1 or respuestasUsuario[intento] > 100:
                print(f"\n¡Mal ahí {nombreUsuario}! \nDebes ingresar un número entre el 1-100.\nQuedan {intentosRestantes} intentos.")
            elif respuestasUsuario[intento] == numeroSecreto:
                print(f"\n¡Has adivinado {nombreUsuario}! \nEl número secreto era: {numeroSecreto} y faltando {intentosRestantes} intentos.")
                acertado = True
                break
            elif respuestasUsuario[intento] > numeroSecreto:
                print(f"\nEquivocado {nombreUsuario}.\nEl número secreto es menor al elegido.\nQuedan {intentosRestantes} intentos.")
            elif respuestasUsuario[intento] < numeroSecreto:
                print(f"\nEquivocado {nombreUsuario}.\nEl número secreto es mayor al elegido.\nQuedan {intentosRestantes} intentos.")
        finally:
            pass

    if not acertado:
        print(f"Caaaaaaaaasi papu.\nEl número secreto era: {numeroSecreto}, para una próxima será...")


def aJugar():
    while True:
        nuevoJuego()
        seguirJugando = input("\n¿Deseas jugar otra vez?\ns: Seguir jugando.\nn: Quiero irme a la camita\ns/n")

        if seguirJugando.lower() == "s":
            aJugar()
        elif seguirJugando.lower() == "n":
            print("Hasta la vista bby")
            break

aJugar()





