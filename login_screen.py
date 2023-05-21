from tkinter import *
from login_script import login


def foto():
    result=login(user_entry2.get(), False)
    if result[2] == "si":
        Label(screen2, text=result[0], fg=result[1], font=("Calibri",11)).pack()

""" def update_label():
    if estat:
        wait_label.config(text="Wait to take the picture...", fg='orange')
    else:
        wait_label.config(text="")  # Si estat es False, ocultar la etiqueta
def execute():
    #threading.Timer(1, execute).start()
    update_label()
    screen2.after(1000, execute) """

def main_window():
    global screen2, user_entry2, wait_label
    screen2 = Tk()
    screen2.title("Login")
    screen2.geometry("300x300")
    Label(screen2, text="Log In").pack()
    Label(screen2, text="").pack()
    verification_user = StringVar()
    # Entrem les dades
    Label(screen2, text="User").pack()
    user_entry2 = Entry(screen2, textvariable=verification_user)
    user_entry2.pack()
    Label(screen2, text="").pack()
    wait_label = Label(screen2, text="Wait to take the picture...", fg='orange', font=("Calibri",11))
    wait_label.pack()
    #update_label()
    Button(screen2, text="Take Foto", width=20, height=1, command=foto).pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Close", width=20, height=1, command=lambda: screen2.destroy()).pack()
    Label(screen2, text="").pack()
    #screen2.after(1000, execute)
    screen2.mainloop()
