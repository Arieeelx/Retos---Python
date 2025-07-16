import tkinter as tk
from tkinter import ttk

def incrementar_barra():
    valor = barra_progreso['value']
    if valor < 100:
        barra_progreso['value'] = valor + 2
        actualizar_porcentaje()

def completar_barra():
    valor = barra_progreso['value']
    if valor < 100:
        barra_progreso['value'] = valor + 10
        actualizar_porcentaje()
        ventana.after(500, completar_barra)

def resetear_barra():
    barra_progreso['value'] = 0
    actualizar_porcentaje()

def actualizar_porcentaje():
    valor = barra_progreso['value']
    porcentaje.set(f'{int(valor)}%')

ventana = tk.Tk()
ventana.title('Barra de Progreso')
ventana.configure(bg="#2b98a6")
ventana.geometry("300x250")

style = ttk.Style()
style.theme_use('alt')
style.configure("TProgressbar", troughcolor="#dfd7ca", background="#c47420", thickness=20)
style.configure("TButton", font=('Helvetica', '10', 'bold'), background="#207eaa", foreground="white")
style.map("TButton", background=[('active', '#1d5670')])

barra_progreso = ttk.Progressbar(ventana, orient="horizontal", length=200, mode="determinate", style="TProgressbar")
barra_progreso.pack(pady=20)

porcentaje = tk.StringVar()
porcentaje.set('0%')

etiqueta_porcentaje = tk.Label(ventana, textvariable=porcentaje, font=('helvetica', 10, 'bold'), bg="#070c0f", fg='white')
etiqueta_porcentaje.pack(pady=10)

boton_incrementar = ttk.Button(ventana, text='Incrementar', command=incrementar_barra, style='TButton')
boton_incrementar.pack(pady=5)

boton_completar = ttk.Button(ventana, text='Completar', command=completar_barra, style='TButton')
boton_completar.pack(pady=5)

boton_resetear = ttk.Button(ventana, text='Resetear', command=resetear_barra, style='TButton')
boton_resetear.pack(pady=5)

ventana.mainloop()

