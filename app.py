import tkinter as tk
from tkinter import filedialog, messagebox, font

class BlocDeNotas:
    def __init__(self, root):
        self.root = root
        self.root.title("Bloc de Notas")
        self.root.geometry("600x400")

        self.text_area = tk.Text(self.root, wrap='word', font=("Arial", 12))
        self.text_area.pack(expand=True, fill='both')

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)
        self.file_menu.add_command(label="Nuevo", command=self.nuevo_archivo)
        self.file_menu.add_command(label="Abrir", command=self.abrir_archivo)
        self.file_menu.add_command(label="Guardar", command=self.guardar_archivo)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=self.root.quit)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Editar", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cambiar Tamaño de Letra", command=self.cambiar_tamano_letra)

    def nuevo_archivo(self):
        self.text_area.delete(1.0, tk.END)

    def abrir_archivo(self):
        archivo = filedialog.askopenfilename(defaultextension=".txt",
                                              filetypes=[("Archivos de Texto", "*.txt"),
                                                         ("Todos los Archivos", "*.*")])
        if archivo:
            with open(archivo, 'r') as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())

    def guardar_archivo(self):
        archivo = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Archivos de Texto", "*.txt"),
                                                            ("Todos los Archivos", "*.*")])
        if archivo:
            with open(archivo, 'w') as file:
                file.write(self.text_area.get(1.0, tk.END))

    def cambiar_tamano_letra(self):
        def aplicar_cambio():
            try:
                tamano = int(entry_tamano.get())
                self.text_area.config(font=("Arial", tamano))
                ventana.destroy()
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingresa un número válido.")

        ventana = tk.Toplevel(self.root)
        ventana.title("Cambiar Tamaño de Letra")
        tk.Label(ventana, text="Tamaño de letra:").pack(pady=10)
        entry_tamano = tk.Entry(ventana)
        entry_tamano.pack(pady=5)
        tk.Button(ventana, text="Aplicar", command=aplicar_cambio).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    bloc_de_notas = BlocDeNotas(root)
    root.mainloop()
