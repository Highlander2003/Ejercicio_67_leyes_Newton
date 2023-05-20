import tkinter as tk
import pygame
from tkinter import messagebox

# Función para calcular la fuerza horizontal
def calcular_fuerza_horizontal():
    # Obtener la masa de los objetos
    masa_objeto1 = float(entry_carretonm.get())
    masa_objeto2 = float(entry_objeto2.get())
    masa_objeto3 = float(entry_objeto3.get())

    # Calcular la fuerza horizontal necesaria
    fuerza_horizontal = round((masa_objeto2 + masa_objeto3) * masa_objeto1 * 9.8, 2)

    # Mostrar el resultado en una ventana emergente
    messagebox.showinfo("Resultado", "La fuerza horizontal necesaria para mantener la masa 1 y masa 2 fijos en relación con el carretón es: \n={} N".format(fuerza_horizontal))

    # Llamar a la función de animación
    animar()

# Función de animación
def animar():
    pygame.init()

    # Obtener el tamaño de la pantalla
    screen_info = pygame.display.Info()
    width = screen_info.current_w-500
    height = screen_info.current_h-500

    # Crear la ventana de animación con el ancho de la pantalla
    screen = pygame.display.set_mode((width, height))

    # Cargar la imagen y redimensionarla
    image = pygame.image.load("vehiculo.png")  # La ruta de tu imagen
    new_width = 650  # Nuevo ancho deseado de la imagen
    new_height = 300  # Nuevo alto deseado de la imagen
    image = pygame.transform.scale(image, (new_width, new_height))

    # Obtener el rectángulo de la imagen para su posicionamiento
    image_rect = image.get_rect()

    # Definir el color de fondo de la ventana
    background_color = (255, 255, 255)

    # Definir las propiedades del objeto animado
    x = 50  # Posición inicial en el eje X
    y = 150  # Posición inicial en el eje Y
    size = 60  # Tamaño del cuadrado
    velocity = 0.5  # Velocidad de movimiento del objeto

    # Definir las propiedades del objeto estático
    x1 = 50
    y1 = 450
    z = -100
    size1 = 10600

    # Bucle principal de la animación
    running = True
    while running:
        # Actualizar la ventana con el color de fondo
        screen.fill((255, 255, 255))  # Blanco

        # Dibujar la imagen en la posición actual
        screen.blit(image, (x, y))
        # Dibujar el cuadrado
        pygame.draw.rect(screen, (158, 80, 6), (z, y1, size1, size1+20000))

        # Actualizar la posición del objeto
        x += velocity

        # Comprobar si el objeto ha alcanzado el borde de la ventana y cambiar su dirección
        if x + image_rect.width > width or x < 0:
            velocity = -velocity

        # Actualizar la pantalla
        pygame.display.flip()

        # Manejar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # Finalizar Pygame
    pygame.quit()
# Crear la ventana principal
root = tk.Tk()
root.title("Fuerza Horizontal")
root.geometry("300x200")  # Tamaño de la ventana emergente (ancho x alto)

# Etiquetas y campos de entrada para las masas
label_carretonm = tk.Label(root, text="Masa del carreton(Kg):")
label_carretonm.pack()
entry_carretonm = tk.Entry(root)
entry_carretonm.pack()

label_objeto2 = tk.Label(root, text="Masa m1 (masa sobre el carreton (Kg)):")
label_objeto2.pack()
entry_objeto2 = tk.Entry(root)
entry_objeto2.pack()

label_objeto3 = tk.Label(root, text="Masa m3 (masa colgando del carreton(Kg)):")
label_objeto3.pack()
entry_objeto3 = tk.Entry(root)
entry_objeto3.pack()

# Botón para calcular la fuerza horizontal
btn_calcular = tk.Button(root, text="Calcular fuerza horizontal", command=calcular_fuerza_horizontal)
btn_calcular.pack()

# Ejecutar la ventana principal
root.mainloop()
