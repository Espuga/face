# Importar llibreries
import cv2 
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
import os
# Importar fitxers
import take_foto
import config


def sign_in(user):
    result = []
    global ruta, reg_face
    # Crear carpeta personal
    # si no existeix, que la crei, si existeix que surti error
    if user in os.listdir(os.path.join(os.getcwd(), 'fotos')):      # si existeix
        result.append(["User alredy exist", "red"])
        #Label(screen1, text="User alredy exist", fg="red", font=("Calibri",11)).pack()
    else:
        os.makedirs(config.files_path+"\\"+user)
    llista = os.listdir(config.files_path+"\\"+user)
    llista = sorted(llista, key=lambda x: int(x.split(".")[0]))
    if len(llista) == 0:
        ruta = config.files_path+"\\"+user+"\\"+'1.jpg'
    else:
        ruta = config.files_path+"\\"+user+"\\"+str(int(llista[len(llista)-1].split(".")[0])+1)+'.jpg'
    print("ultim: " + str(llista[len(llista)-1]))
    cv2.imwrite(ruta, take_foto.take(user, "register"))
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
    result.append(["FaceID Registration SUCCESSFULLY", "green"])
    return result
