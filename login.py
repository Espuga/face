from tkinter import *
import cv2 
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
import take_foto
import config
import os

def login():
    #print("abans take_foto.take")
    cv2.imwrite(config.files_path+"\\log\\"+user_entry2.get()+'_LOG.jpg', take_foto.take('login'))
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
            cv2.imwrite(config.files_path+"\\log\\"+user_entry2.get()+'_LOG.jpg', face_reg)
            #Plotejem les cares
            pyplot.imshow(data[y1:y2, x1:x2])
        pyplot.show(block=False)
        pyplot.close()
    img = config.files_path+"\\log\\"+user_entry2.get()+"_LOG.jpg"
    pixels = pyplot.imread(img)
    detector = MTCNN()
    faces = detector.detect_faces(pixels)
    reg_face(img, faces)
    def orb_sim(img1, img2):
        orb = cv2.ORB_create()  # Crear el objecte de comparació
        # Extreu punts clau de img1 i img2
        kpa, descr_a = orb.detectAndCompute(img1, None)
        kpa, descr_b = orb.detectAndCompute(img2, None)
        comp = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)   # Crear el comparador de força
        matches = comp.match(descr_a, descr_b)      # Aplicem el comparador als descriptors
        similar_regions = [i for i in matches if i.distance < 70]   # Extreu les regions similars en base als punts clau
        if len(matches) == 0:
            return 0
        return len(similar_regions)/len(matches)    # Exportar el percentatge de similitud
    # Importar les imatges i cridar a la funció de comparacio
    im_files = os.listdir(os.path.join(os.getcwd(), 'fotos'))     # Llistar els arxius de la carpeta fotos
    if user_entry2.get() in im_files:
        face_log = cv2.imread(config.files_path+"\\log\\"+user_entry2.get()+"_LOG.jpg",0)
        for image in os.listdir(config.files_path+"\\"+user_entry2.get()):
            print("====================")
            face_reg = cv2.imread(config.files_path+"\\"+user_entry2.get()+"\\"+image.split(".")[0]+".jpg",0)
            similar = orb_sim(face_reg, face_log)
            print("Compatibility", image.split(".")[0]+": " + str(round(similar, 2)))
            if similar >= 0.9:
                Label(screen2, text="Log In SUCCESFULLY\n Compatibility: "+str(round(similar*100, 4))+"%", fg="green", font=("Calibri",11)).pack()
                print("Welcome into the system")
                break
        else:
            print("Bad face")
            Label(screen2, text="Log In FAILED", fg="red", font=("Calibri",11)).pack()
    else:
        print("User not found")
        Label(screen2, text="User not found", fg="red", font=("Calibri",11)).pack()
    os.remove(config.files_path+"\\log\\"+user_entry2.get()+"_LOG.jpg")


def main_window():
    global screen2, user_entry2
    screen2 = Tk()
    screen2.title("Login")
    screen2.geometry("300x300")
    Label(screen2, text="Log In").pack()
    Label(screen2, text="").pack()
    verification_user = StringVar()
    # Entrem les dades
    Label(screen2, text="User * ").pack()
    user_entry2 = Entry(screen2, textvariable=verification_user)
    user_entry2.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Take Foto", width=20, height=1, command=login).pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Close", width=20, height=1, command=lambda: screen2.destroy()).pack()