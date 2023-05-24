# Importar llibreries
from tkinter import *
# Importar fitxers
from login_script import login
import config

comp = False
# Funcio retornar si login succcesfully o no
def foto():
    global comp 
    comp = True
    result=login(user_entry2.get())
    if result[2] == "si":
        Label(screen2, text=result[0], fg=result[1], font=("Calibri",11)).pack()

# Inici funcions per acualitzar la pagina
update = True
def update_label():
    global update
    if update:
        from config import estat
        if estat:
            wait_label.config(text="Wait to take the picture...", fg='orange')
        else:
            wait_label.config(text="You can take the foto", fg='green')
            wait_button.config(state="active")
            update = False
def execute():
    if update:
        update_label()
        screen2.after(1000, execute)
# Final funcions per acualitzar

def destruir():
    if config.cap.isOpened() and comp:
        print("Esta oberta")
        import threading
        config.cap.release()
        fil = threading.Thread(target=lambda: config.cargar())
        fil.start()
    else:
        print("No esta oberta")
    screen2.destroy()

def main_window():
    global screen2, user_entry2, wait_label, wait_button
    # Configuració pantalla
    screen2 = Tk()
    screen2.title("Login")
    screen2.geometry("300x300")
    # Plantilla
    Label(screen2, text="Log In").pack()
    Label(screen2, text="").pack()
    verification_user = StringVar()
    Label(screen2, text="User").pack()
    user_entry2 = Entry(screen2, textvariable=verification_user)
    user_entry2.pack()
    Label(screen2, text="").pack()
    wait_label = Label(screen2, text="", font=("Calibri",11))
    wait_label.pack()
    wait_button = Button(screen2, text="Take Foto", width=20, height=1, command=foto)
    wait_button.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Close", width=20, height=1, command=destruir).pack()
    Label(screen2, text="").pack()
    # Acualitzar pagina per quan es carregui la camera
    execute()
    screen2.mainloop()
