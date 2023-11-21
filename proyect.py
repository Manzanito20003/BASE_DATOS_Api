import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import psycopg2

def agregar_persona():
    cedula = entry_cedula.get()
    nombre = entry_nombre.get()
    telefono = entry_telefono.get()
    genero = entry_genero.get()
    edad = entry_edad.get()
    esquema = entry_esquema.get()

    try:
        # Obtener los valores de los campos de entrada de la conexión
        host = entry_host.get()
        database = entry_database.get()
        user = entry_user.get()
        password = entry_password.get()

        # Crear la conexión
        with psycopg2.connect(host=host, database=database, user=user, password=password) as conexion:
            with conexion.cursor() as cursor:
                # Ejemplo de inserción de persona en un esquema especificado por el usuario
                cursor.execute("INSERT INTO {}.persona VALUES (%s, %s, %s, %s, %s)".format(esquema),
                               (edad, nombre, telefono, genero, cedula))
            conexion.commit()
            messagebox.showinfo("Éxito", "Persona agregada con éxito.")

    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")

def ver_base_datos():
    try:
        # Obtener los valores de los campos de entrada de la conexión
        host = entry_host.get()
        database = entry_database.get()
        user = entry_user.get()
        password = entry_password.get()
        esquema = entry_esquema.get()

        # Crear la conexión
        with psycopg2.connect(host=host, database=database, user=user, password=password) as conexion:
            with conexion.cursor() as cursor:
                # Ejemplo de consulta para obtener todas las personas del esquema especificado
                cursor.execute("SELECT * FROM {}.persona".format(esquema))
                personas = cursor.fetchall()

                # Crear una nueva ventana para mostrar los resultados
                ventana_resultados = tk.Toplevel(ventana)
                ventana_resultados.title("Resultados de la Base de Datos")

                # Crear un widget Treeview para mostrar los datos
                tree = ttk.Treeview(ventana_resultados)
                tree["columns"] = ("Cédula", "Nombre", "Teléfono", "Género", "Edad")

                # Configurar las columnas
                tree.column("#0", width=0, stretch=tk.NO)
                tree.column("Edad", anchor=tk.W, width=100)
                tree.column("Nombre", anchor=tk.W, width=150)
                tree.column("Teléfono", anchor=tk.W, width=100)
                tree.column("Género", anchor=tk.W, width=80)
                tree.column("Dni", anchor=tk.W, width=50)

                # Encabezados de las columnas
                tree.heading("#0", text="", anchor=tk.W)
                tree.heading("Edad", text="Cédula", anchor=tk.W)
                tree.heading("Nombre", text="Nombre", anchor=tk.W)
                tree.heading("Teléfono", text="Teléfono", anchor=tk.W)
                tree.heading("Género", text="Género", anchor=tk.W)
                tree.heading("Dni", text="Edad", anchor=tk.W)

                # Insertar datos en el Treeview
                for persona in personas:
                    tree.insert("", tk.END, values=persona)

                tree.pack(expand=tk.YES, fill=tk.BOTH)

    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Agregar Persona")

# Crear un estilo para mejorar la apariencia
style = ttk.Style()
style.configure("TLabel", padding=5, font=("Helvetica", 11))
style.configure("TButton", padding=10, font=("Helvetica", 11))

# Crear etiquetas y campos de entrada
etiqueta_host = ttk.Label(ventana, text="Host:")
etiqueta_host.grid(column=0, row=0, padx=10, pady=10, sticky=tk.W)

entry_host = ttk.Entry(ventana)
entry_host.grid(column=1, row=0, padx=10, pady=10, sticky=tk.W)

etiqueta_database = ttk.Label(ventana, text="Base de Datos:")
etiqueta_database.grid(column=0, row=1, padx=10, pady=10, sticky=tk.W)

entry_database = ttk.Entry(ventana)
entry_database.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)

etiqueta_esquema = ttk.Label(ventana, text="Esquema:")
etiqueta_esquema.grid(column=0, row=2, padx=10, pady=10, sticky=tk.W)

entry_esquema = ttk.Entry(ventana)
entry_esquema.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)

etiqueta_user = ttk.Label(ventana, text="Usuario:")
etiqueta_user.grid(column=0, row=3, padx=10, pady=10, sticky=tk.W)

entry_user = ttk.Entry(ventana)
entry_user.grid(column=1, row=3, padx=10, pady=10, sticky=tk.W)

etiqueta_password = ttk.Label(ventana, text="Contraseña:")
etiqueta_password.grid(column=0, row=4, padx=10, pady=10, sticky=tk.W)

entry_password = ttk.Entry(ventana, show="*")  # Para ocultar la contraseña
entry_password.grid(column=1, row=4, padx=10, pady=10, sticky=tk.W)

etiqueta_edad = ttk.Label(ventana, text="Edad:")
etiqueta_edad.grid(column=0, row=5, padx=10, pady=10, sticky=tk.W)

entry_edad = ttk.Entry(ventana)
entry_edad.grid(column=1, row=5, padx=10, pady=10, sticky=tk.W)

etiqueta_nombre = ttk.Label(ventana, text="Nombre:")
etiqueta_nombre.grid(column=0, row=6, padx=10, pady=10, sticky=tk.W)

entry_nombre = ttk.Entry(ventana)
entry_nombre.grid(column=1, row=6, padx=10, pady=10, sticky=tk.W)

etiqueta_telefono = ttk.Label(ventana, text="Teléfono:")
etiqueta_telefono.grid(column=0, row=7, padx=10, pady=10, sticky=tk.W)

entry_telefono = ttk.Entry(ventana)
entry_telefono.grid(column=1, row=7, padx=10, pady=10, sticky=tk.W)

etiqueta_genero = ttk.Label(ventana, text="Género:")
etiqueta_genero.grid(column=0, row=8, padx=10, pady=10, sticky=tk.W)

# Menú desplegable para seleccionar el género
genero_options = ["Masculino", "Femenino"]
entry_genero = ttk.Combobox(ventana, values=genero_options)
entry_genero.grid(column=1, row=8, padx=10, pady=10, sticky=tk.W)

etiqueta_cedula = ttk.Label(ventana, text="Cédula:")
etiqueta_cedula.grid(column=0, row=9, padx=10, pady=10, sticky=tk.W)

entry_cedula = ttk.Entry(ventana)
entry_cedula.grid(column=1, row=9, padx=10, pady=10, sticky=tk.W)

# Botón para agregar persona
boton_agregar = ttk.Button(ventana, text="Agregar Persona", command=agregar_persona)
boton_agregar.grid(column=0, row=10, columnspan=2, pady=10)

# Botón para ver la base de datos
boton_ver_db = ttk.Button(ventana, text="Ver Base de Datos", command=ver_base_datos)
boton_ver_db.grid(column=0, row=11, columnspan=2, pady=10)

# Ajustar el tamaño de las columnas
for child in ventana.winfo_children():
    child.grid_configure(padx=8, pady=8)

# Iniciar el bucle de la interfaz gráfica
ventana.mainloop()

