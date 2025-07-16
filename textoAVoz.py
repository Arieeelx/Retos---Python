from gtts import gTTS
import os

texto = "Hola mundo, aprendiendo Python nuevamente jeje"

output = gTTS(texto, lang="es", slow=False)
output.save("output.mp3")

os.system('start output.mp3')