from tkinter import * 
import cv2
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
import take_foto
import config
import os

def sign_in():
    global ruta, user_entry, reg_face
    # Crear carpeta personal
    # si no existeix, que la crei, si existeix que surti error
    if user_entry.get() in os.listdir(os.path.join(os.getcwd(), 'fotos')):      # si existeix
        Label(screen1, text="User alredy exist", fg="red", font=("Calibri",11)).pack()
    else:
        os.makedirs(config.files_path+"\\"+user_entry.get())
    llista = os.listdir(config.files_path+"\\"+user_entry.get())
    if len(llista) == 0:
        ruta = config.files_path+"\\"+user_entry.get()+"\\"+'1.jpg'
    else:
        ruta = config.files_path+"\\"+user_entry.get()+"\\"+str(int(llista[len(llista)-1].split(".")[0])+1)+'.jpg'
    cv2.imwrite(ruta, take_foto.take(user_entry.get()))
    def reg_face(img, list_results):
        data = pyplot.imread(img)
        for i in range(len(list_results)):
            # Obtenir cordenades
            x1, y1, ample1, alçada1 = list_results[i]['box']
            x2, y2 = x1 + ample1, y1 + alçada1
            # Definir el subplot
            pyplot.subplot(1, len(list_results), i+1)
            pyplot.axis('off')
            face_reg = data[y1:y2, x1:x2]
            face_reg = cv2.resize(face_reg, (150,200), interpolation=cv2.INTER_CUBIC)   # Guardar la imatge 
            cv2.imwrite(ruta, face_reg)
            #Plotejem les cares
            pyplot.imshow(data[y1:y2, x1:x2])
        pyplot.show(block=False)
        pyplot.close()
    img = ruta
    pixels = pyplot.imread(img)
    detector = MTCNN()
    faces = detector.detect_faces(pixels)
    reg_face(img, faces)
    Label(screen1, text="FaceID Registration SUCCESSFULLY", fg="green", font=("Calibri",11)).pack()

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
    Button(screen1, text="FaceID Sign In", width=15, height=1, command=sign_in).pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Close", width=15, height=1, command=lambda: screen1.destroy()).pack()