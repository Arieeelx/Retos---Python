import tkinter as tk
from tkinter import messagebox
import pandas as pd
import random

file_path = '06 - Preguntas.xlsx'
data = pd.read_excel(file_path)
data = data.astype(str)

# FUNCIÓN PARA INICIAR EL JUEGO

def start_game():
    global question_index, correct_answers
    question_index = 0
    correct_answers = 0
    show_question()

def show_question():
    if question_index < len(data):
        options = [data['Respuesta Correcta'][question_index], data['R1'][question_index],
                   data['R2'][question_index], data['R3'][question_index]]
        random.shuffle(options)

        question_label.config(text=data['Pregunta'][question_index])
        for i in range(4):
            radio_button[i].config(text=options[i], value=options[i])
        update_status()
    else:
        messagebox.showinfo("Fin del juego",
                            f"Juego terminado! Respondiste {correct_answers} preguntas correctamente de {len(data)}.")
        root.destroy()

def update_status():
    status_label.config(text=f"Pregunta {question_index + 1} de {len(data)}")

def handle_answer():
    global question_index, correct_answers
    if answer_var.get() == data['Respuesta Correcta'][question_index]:
        correct_answers += 1
    else:
        messagebox.showerror("Respuesta incorrecta",
                             f"Incorrecto! La respuesta correcta era: {data['Respuesta Correcta'][question_index]}")
    question_index += 1
    show_question()

root = tk.Tk()
root.title("Trivia")

# VARIABLES
question_index = 0
correct_answers = 0
answer_var = tk.StringVar()

# WIDGETS
question_label = tk.Label(root, text="", wraplength=400)
question_label.pack(pady=(20, 10))

radio_button = []
for _ in range(4):
    rb = tk.Radiobutton(root, text="", variable=answer_var, wraplength=300)
    rb.pack(anchor="w")
    radio_button.append(rb)

answer_button = tk.Button(root, text="Responder", command=handle_answer)
answer_button.pack(pady=20)

status_label = tk.Label(root, text="")
status_label.pack()

start_game()
root.mainloop()