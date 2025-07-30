import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import qrcode

class mi_QR():
    def __init__(self, master, size=30, padding=2):
        self.master = master
        self.qr = qrcode.QRCode(box_size=size, border=padding)

    def crear_QR(self, nombreArchivo, fg, bg):
        ingresarEnlace = simpledialog.askstring("Entrada", "Introduce el texto para el código QR:", parent=self.master)
        try:
            self.qr.add_data(ingresarEnlace)
            self.qr.make(fit=True)
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(nombreArchivo)

            messagebox.showinfo("Completado", f"Se creó exitosamente tú código QR: {nombreArchivo}")

        except Exception as e:

            messagebox.showerror("Error", f"Ocurrió un error: {e}")

root = tk.Tk()
root.geometry("200x200")
root.title("Creador de QR")
app = mi_QR(root)
boton = tk.Button(root, text="Crear código QR", command=lambda: app.crear_QR('QR.png', fg='white', bg='black'))
boton.pack(pady=10)


root.mainloop()