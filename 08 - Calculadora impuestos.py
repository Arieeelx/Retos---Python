import customtkinter as ctk

class calculadoraImpuestos:
    def __init__(self):
        self.ventana = ctk.CTk()
        self.ventana.title("Calculadora de Impuestos")
        self.ventana.config(bg="#262423")
        self.ventana.geometry("350x250")
        self.ventana.resizable(False, False)
        self.padding: dict = {'padx': 20, 'pady':10}
        self.font = ("Arial", 12)

        self.etiqueta_ingreso = ctk.CTkLabel(self.ventana, text='Ingreso:', font=self.font, bg_color="#262423")
        self.etiqueta_ingreso.grid(row=0, column=0, **self.padding)
        self.entrada_ingreso = ctk.CTkEntry(self.ventana, font=self.font)
        self.entrada_ingreso.grid(row=0, column=1, **self.padding)

        self.etiqueta_porcentaje = ctk.CTkLabel(self.ventana, text='Porcentaje:', font=self.font, bg_color="#262423")
        self.etiqueta_porcentaje.grid(row=1, column=0, **self.padding)
        self.entrada_porcentaje = ctk.CTkEntry(self.ventana, font=self.font)
        self.entrada_porcentaje.grid(row=1, column=1, **self.padding)

        self.etiqueta_impuesto = ctk.CTkLabel(self.ventana, text='Impuesto:', font=self.font, bg_color="#262423")
        self.etiqueta_impuesto.grid(row=2, column=0, **self.padding)
        self.entrada_impuesto = ctk.CTkEntry(self.ventana, font=self.font)
        self.entrada_impuesto.insert(0, '0')
        self.entrada_impuesto.grid(row=2, column=1, **self.padding)

        self.boton_calcular = ctk.CTkButton(self.ventana, text="Calcular", font=self.font,
                                            command=self.calcular_impuesto)
        self.boton_calcular.grid(row=3, column=1, **self.padding)

    def actualizar_resultado(self, texto):
        self.entrada_impuesto.insert(0, texto)

    def calcular_impuesto(self):
        self.entrada_impuesto.delete(0, ctk.END)
        try:
            ingreso: float = float(self.entrada_ingreso.get())
            porcentaje: float = float(self.entrada_porcentaje.get())
            self.actualizar_resultado(f"${ingreso * (porcentaje / 100):,.1f}")
        except ValueError:
            self.actualizar_resultado('Entrada inválida')
    def ejecutar(self):
        self.ventana.mainloop()

calculadora = calculadoraImpuestos()
calculadora.ejecutar()
