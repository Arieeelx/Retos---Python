import tkinter as tk
import random
from tkinter import scrolledtext

def caracteristicas_dado(cant_dado, caras_dado):
    return [random.randint(1, caras_dado) for _ in range(cant_dado)]
def lanzar_dados():
    cant_dado = entry.get().strip()
    if cant_dado.isdigit():
        cant_dado = int(cant_dado)
        caras_dado = int(cantidadD_var.get())
        rolls = caracteristicas_dado(cant_dado, caras_dado)
        total = sum(rolls)
        resultadoTexto.delete('1.0', tk.END)
        resultadoTexto.insert(tk.INSERT, f"Resultados: {rolls}\n")


app = tk.Tk()
app.title("Lanzador de dados")
app.config(bg="#261212")
app.geometry("600x500")

font_large = ("Arial", 16)
font_extra_large = ("Arial", 20)

entry_label = tk.Label(app, text="¿Cuántos dados quieres lanzar?", bg="#261212",
                       fg='white', font=font_large)
entry_label.pack()
entry = tk.Entry(app, font=font_large)
entry.pack()

cantidadD_label = tk.Label(app, text="Selecciona el tipo de dado:", bg="#261212",
                       fg='white', font=font_large)
cantidadD_label.pack()

cantidadD_var = tk.StringVar(app)
cantidadD_var.set("6")
cantidadD_options = tk.OptionMenu(app, cantidadD_var, "4",
                                  "6", "8", "10", "12", "20", "100")
cantidadD_options.config(font=font_large)
cantidadD_options.pack()

lanzarDados = tk.Button(app, text="Lanzar dados", command=lanzar_dados, bg="black",
                        fg='white', font=font_large)
lanzarDados.pack()

resultadoTexto = scrolledtext.ScrolledText(app, width=40, height=10, font=font_large,
                                           bg='white', fg='black')
resultadoTexto.pack()

totalResultado = tk.Label(app, text="", bg="#261212", fg='gold', font=font_extra_large)
totalResultado.pack()



app.mainloop()