import tkinter as tk

def calcular_dias():
    nombre = entry_nombre.get()
    try:
        edad = int(entry_edad.get())
    except ValueError:
        resultado_label.config(text="Por favor, ingresa un número válido para la edad.", fg="red")
        return
    dias_vividos = edad * 365
    resultado_label.config(text=f"{nombre}, has vivido aproximadamente {dias_vividos} días.", fg="green")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Calculador de Días Vividos")

# Etiqueta y entrada para el nombre
tk.Label(root, text="¿Cuál es tu nombre?").grid(row=0, column=0, padx=10, pady=10)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1, padx=10, pady=10)

# Etiqueta y entrada para la edad
tk.Label(root, text="¿Cuántos años tienes?").grid(row=1, column=0, padx=10, pady=10)
entry_edad = tk.Entry(root)
entry_edad.grid(row=1, column=1, padx=10, pady=10)

# Botón para calcular
tk.Button(root, text="Calcular", command=calcular_dias).grid(row=2, column=0, columnspan=2, pady=10)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(root, text="")
resultado_label.grid(row=3, column=0, columnspan=2, pady=10)

# Iniciar la aplicación
root.mainloop()