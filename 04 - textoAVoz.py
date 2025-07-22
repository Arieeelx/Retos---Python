from gtts import gTTS
import os

with open('textoaleer.txt', 'r', encoding="utf-8") as file:
    texto = file.read()

audio = gTTS(texto, lang="es", slow="False")
audio.save("output.mp3")

os.system('start output.mp3')