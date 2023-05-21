from tkinter import * 
from register_script import sign_in

def register():
    result=sign_in(user_entry.get())
    for c1 in result:
       Label(screen1, text=c1[0], fg=c1[1], font=("Calibri",11)).pack()

def main_window():
    global user_entry, screen1
    #screen1 = Toplevel(screen)      # Aquesta pantalla nivell superior a la principal
    screen1 = Tk()
    screen1.title("Sign In")
    screen1.geometry("300x300")
    # Crear entrades
    user = StringVar()
    # Pantalla
    Label(screen1, text="Register").pack()
    Label(screen1, text="").pack()      # Separar
    Label(screen1, text="User").pack()
    user_entry = Entry(screen1, textvariable=user)      # Crear un text variable per que el user entri la info
    user_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="FaceID Sign In", width=15, height=1, command=register).pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Close", width=15, height=1, command=lambda: screen1.destroy()).pack()