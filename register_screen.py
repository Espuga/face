# Importar llibreries
from tkinter import * 
# Importar fitxers
from register_script import sign_in
import config

comp = False
# Funció per retornar si registre exitos
def register():
    global comp
    comp = True
    result=sign_in(user_entry.get())
    for c1 in result:
       Label(screen1, text=c1[0], fg=c1[1], font=("Calibri",11)).pack()

# Inici acualitzar pantalla per quan la camara estigui carregada
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
        screen1.after(1000, execute)
# Final acualitzar pantalla

def destruir():
    if config.cap.isOpened() and comp:
        import threading
        config.estat = True
        config.cap.release()
        fil = threading.Thread(target=lambda: config.cargar())
        fil.start()
    screen1.destroy()



def main_window():
    global user_entry, screen1, wait_label, wait_button
    # Config screen1
    screen1 = Tk()
    screen1.title("Sign In")
    screen1.geometry("300x300")
    # Crear entrades
    user = StringVar()
    # Pantalla
    Label(screen1, text="Register").pack()
    Label(screen1, text="").pack()    
    Label(screen1, text="User").pack()
    user_entry = Entry(screen1, textvariable=user) 
    user_entry.pack()
    Label(screen1, text="").pack()
    wait_label = Label(screen1, text="", font=("Calibri",11))
    wait_label.pack()
    wait_button =  Button(screen1, text="Take Foto", width=15, height=1, command=register)
    wait_button.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Close", width=15, height=1, command=destruir).pack()
    # Funcio per acualitzar quan la camera estigui carregada
    execute()
    screen1.mainloop()