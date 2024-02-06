import tkinter as tk
from tkinter import ttk

def enviar_formulario():
    seleccion = combo.get()
    valor_app1 = entry_app1.get()
    valor_app2 = entry_app2.get()
    valor_rol = entry_rol.get()

    # Puedes realizar acciones con los valores del formulario aquí
    print("Entorno:", seleccion)
    print("App1:", valor_app1)
    print("App2:", valor_app2)
    print("Rol:", valor_rol)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Creación Usuarios WS")


# Etiquetas y campos de entrada
tk.Label(ventana, text="App1:").grid(row=1, column=0, pady=10, padx=10)
entry_app1 = tk.Entry(ventana)
entry_app1.grid(row=1, column=1, pady=10, padx=10)


# App Destino
tk.Label(ventana, text="App Destino:").grid(row=2, column=0, pady=10, padx=10)
entry_app2 = tk.Entry(ventana)
entry_app2.grid(row=2, column=1, pady=10, padx=10)

opciones = ["PORTAFIB", "NOTIB", "ROLSAC", "PORTAFIB", "ASNOTIF", "PINBAL", "LOGINIB", "DIR3CAIB", "CIVITAS", "SIFARMA" ]
combo = ttk.Combobox(ventana, values=opciones)
combo.set(opciones[0])  # Establecer el valor predeterminado
combo.grid(row=2, column=1, pady=10, padx=10)

# Entorno
tk.Label(ventana, text="Entorno:").grid(row=3, column=0, pady=10, padx=10)

opciones = ["DES", "PRE", "PRO"]
combo = ttk.Combobox(ventana, values=opciones)
combo.set(opciones[0])  # Establecer el valor predeterminado
combo.grid(row=3, column=1, pady=10, padx=10)

tk.Label(ventana, text="Rol:").grid(row=4, column=0, pady=10, padx=10)
entry_rol = tk.Entry(ventana)
entry_rol.grid(row=4, column=1, pady=10, padx=10)

# Botón para enviar el formulario
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_formulario)
boton_enviar.grid(row=5, column=0, columnspan=2, pady=10)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
