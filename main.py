import login
import register
from tkinter import *

def main_screen():
    global screen   # Globalitzem la variable per ferla servir en altres funcions
    screen = Tk()
    screen.geometry("300x250")
    screen.title("FaceID")
    Label(text="FaceID", bg="gray", width="300", height="2", font=("Verdana",13)).pack()
    # Crear botons
    Label(text="").pack()   # Espai entre el titol i primer boto
    Button(text="Log In", height="2", width="30", command=login.main_window).pack()   # Iniciar secio
    Label(text="").pack()   # Espai entre botons
    Button(text="Sign In", height="2", width="30", command=register.main_window).pack()   # Registrar-se
    Label(text="").pack()
    Button(text="Close", height="2", width="30", command=lambda: screen.destroy()).pack()

    screen.mainloop()

main_screen()