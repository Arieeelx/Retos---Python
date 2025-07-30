import time
import pygame
import sys

pygame.init()

#Config de pantalla
anchoPantalla = 640
altoPantalla = 480

#Colores
negro = "#000000"
blanco = "#ffffff"

#Fuente
fuente = pygame.font.Font(None, 74)

pantalla = pygame.display.set_mode((anchoPantalla, altoPantalla))
pygame.display.set_caption("Temporizador de Alarma")

def mostrar_tiempo_restante(segundosRestantes):
    pantalla.fill(negro)
    minutosRestantes = segundosRestantes // 60
    segundosRestantes = segundosRestantes % 60
    tiempoFormateado = f"{minutosRestantes:02d}:{segundosRestantes:02d}"
    texto = fuente.render(tiempoFormateado, True, blanco)
    rect_texto = texto.get_rect(center=(anchoPantalla // 2, altoPantalla // 2))
    pantalla.blit(texto, rect_texto)
    pygame.display.flip()

def alarma(segundos):
    tiempoInicial = time.time()
    tiempoTranscurrido = 0

    while tiempoTranscurrido < segundos:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        tiempoActual = time.time()
        tiempoTranscurrido = tiempoActual - tiempoInicial
        segundosRestantes = int(segundos - tiempoTranscurrido)
        mostrar_tiempo_restante(segundosRestantes)
        time.sleep(1)

    pygame.mixer.init()
    pygame.mixer.music.load("09_Alarma de despertador.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        time.sleep(1)


minutos = int(input("Ingrees minutos: "))
segundos = int(input("Ingrese los segundos: "))
segundosTotales = minutos * 60 + segundos
alarma(segundosTotales)
