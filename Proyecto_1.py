import tkinter as tk
import string
import random

root=tk.Tk()
root.title("Generador de contraseñas")
root.geometry("500x400")


def crear_contraseña():
    caracter = entrada.get()
    #Cadena de texto
    options = string.ascii_letters + string.punctuation + string.digits
    #numeros random 
    caracter = int(caracter)
    choice = ""
    for i in range(caracter):
        choice += options[random.choice(range(len(options)))]

    print(choice)



label1=tk.Label(root, text="selecciona para generar contraseña ", font=("Arial", 20)) 
label1.pack(padx=20, pady=20)

button1=tk.Button(root, text="Generar contraseña",font=("Arial", 11) )
button1.pack(padx=6, pady=12)

      

# Crear un label
label = tk.Label(root, text="Ingresa de cuantos caracteres quieres que sea la contraseña:")
label.pack(pady=10)



# Crear un campo de entrada
# Crear un String bar
string_var = tk.StringVar(root, text="entrada")
entrada = tk.Entry(root, textvariable=string_var, width=40)
entrada.pack(pady=10)





# Crear un botón
boton = tk.Button(root, text="Enviar", command=crear_contraseña)
boton.pack(pady=10)


root.mainloop()