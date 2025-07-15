import tkinter as tk
from tkinter import messagebox

jugador = "X"
juegoTerminado = False

def chequear_ganador():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    return False

def click_boton(fila, columna):
    global jugador, juegoTerminado

    if buttons[fila][columna]["text"] == "" and not juegoTerminado:
        buttons[fila][columna]["text"] = jugador
        buttons[fila][columna]["bg"] = "#5d6d7e" if jugador == "X" else "#2c3e50"

        if chequear_ganador():
            messagebox.showinfo("El", f"Jugador {jugador} gana!")
            juegoTerminado = True

        elif all(buttons[fila][columna]["text"] != "" for fila in range(3) for columna in range(3)):
            messagebox.showinfo("El gato", "¡Es un empate!")
            juegoTerminado = True

        else:
            jugador = "O" if jugador == "X" else "X"

def reiniciar_juego():
    global jugador, juegoTerminado

    jugador = "X"
    juegoTerminado = False

    for fila in range(3):
        for columna in range(3):
            buttons[fila][columna]["text"] = ""
            buttons[fila][columna]["bg"] = "#1c2833"


root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("400x450")
root.configure(bg="#515a5a")

frame = tk.Frame(root, bg="#1c2833")
frame.place(relx=0.5, rely=0.5, anchor="center")

buttons = [[tk.Button(frame, text="", font="italic", width=5, height=5, bg="#1c2833", fg="white", command=lambda row=fila, col=columna: click_boton(fila, columna))
            for columna in range(3)] for fila in range(3)]

root.mainloop()




