import cv2
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
import os
from config import files_path
 
def normalize_image(image):
    # Converitr la image a escala de grisos
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Aplicar la normalització de brillo i contrast
    normalized = cv2.normalize(gray, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    # Convertir la imatge a RGB
    normalized = cv2.cvtColor(normalized, cv2.COLOR_GRAY2BGR)
    return normalized
def reg_face(img, list_results, ruta):
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
            pyplot.close()
        pyplot.show(block=False)
        pyplot.close()



def take(user, from_):
    #cap = cv2.VideoCapture(0)
    from config import cap

    while True:
        ret,frame = cap.read()
        cv2.imshow('FaceID',frame)

        # Espai per fer foto
        if cv2.waitKey(1) == 32:
            llista = os.listdir(files_path+"\\"+user)
            llista = sorted(llista, key=lambda x: int(x.split(".")[0]))
            if len(llista) == 0:
                ruta = files_path+"\\"+user+"\\"+'1.jpg'
            else:
                ruta = files_path+"\\"+user+"\\"+str(int(llista[len(llista)-1].split(".")[0])+1)+'.jpg'
            cv2.imwrite(ruta, normalize_image(frame))
            img = ruta
            pixels = pyplot.imread(img)
            detector = MTCNN()
            faces = detector.detect_faces(pixels)
            reg_face(img, faces, ruta)
        if cv2.waitKey(1) == 27:
            break
    #cap.release()
    cv2.destroyAllWindows()
    return normalize_image(frame)