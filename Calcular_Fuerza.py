import tkinter as tk
from tkinter import messagebox

# Función para calcular la fuerza horizontal
def calcular_fuerza_horizontal():
    # Obtener la masa de los objetos
    masa_objeto1 = float(entry_objeto1.get())
    masa_objeto2 = float(entry_objeto2.get())
    masa_objeto3 = float(entry_objeto3.get())

    # Calcular la fuerza horizontal necesaria
    fuerza_horizontal = round((masa_objeto2 + masa_objeto3) * masa_objeto1 * 9.8, 2)

    # Mostrar el resultado en una ventana emergente
    messagebox.showinfo("Resultado", "La fuerza horizontal necesaria para mantener la masa 1 y masa 2 fijos en relación con el carreton es: {} N".format(fuerza_horizontal))

# Crear la ventana principal
root = tk.Tk()
root.title("Fuerza Horizontal")
root.geometry("300x200")  # Tamaño de la ventana emergente (ancho x alto)

# Etiquetas y campos de entrada para las masas
label_objeto1 = tk.Label(root, text="Masa del carreton:")
label_objeto1.pack()
entry_objeto1 = tk.Entry(root)
entry_objeto1.pack()

label_objeto2 = tk.Label(root, text="Masa m1 (masa sobre el carreton):")
label_objeto2.pack()
entry_objeto2 = tk.Entry(root)
entry_objeto2.pack()

label_objeto3 = tk.Label(root, text="Masa m3 (masa colgando del carreton):")
label_objeto3.pack()
entry_objeto3 = tk.Entry(root)
entry_objeto3.pack()

# Botón para calcular la fuerza horizontal
btn_calcular = tk.Button(root, text="Calcular fuerza horizontal", command=calcular_fuerza_horizontal)
btn_calcular.pack()

# Ejecutar la ventana principal
root.mainloop()

