import os
from tkinter import Tk, Text, Button, END, Label
from gtts import gTTS

def save_text():
    text = text_area.get("1.0", END)
    with open('04 - user_input.txt', 'w', encoding="utf-8") as file:
        file.write(text)

    status_label.config(text="Texto guardado con éxito.")

def text_to_speech():
    text = text_area.get("1.0", END)
    speech = gTTS(text=text, lang='es', slow=False)
    speech.save('output_04.mp3')
    os.system('start output_04.mp3')

    status_label.config(text='Reproduciendo audio.')

ventana = Tk()
ventana.title("Texto a voz")
ventana.configure(bg="#dbdbde")

text_area = Text(ventana, height=10, width=50)
text_area.pack()

save_button = Button(ventana, text="Guardar texto", command=save_text)
save_button.pack()

play_button = Button(ventana, text="Reproducir texto", command=text_to_speech)
play_button.pack()

status_label = Label(ventana, text="", fg="#cf5630", bg="#dbdbde")
status_label.pack()

ventana.mainloop()